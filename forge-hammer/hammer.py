import secrets
import fire
import logging
import doctl_liip
import helpers
import gitlab
from cookiecutter.main import cookiecutter

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def create_do_resources(project_name: str, public_deploy_ssh_key: str, personal_ssh_key_fingerprint: str):
    """
    Create DO resources required for a new project. Droplet, Domain, SSH keys

    :param project_name: Name of project
    :param public_deploy_ssh_key: Public deploy ssh key to be added to droplet. (Allows gitlab to deploy)
    :param personal_ssh_key_fingerprint: SSH key fingerprint of personal SSH key on DO. . (Allows you SSH access).
        This can be created/retreived from Settings -> Security on the DO dashboard
    """
    project_name_formatted = project_name.lower().replace(' ', '')
    project_domain = f'{project_name_formatted}-dev.bedev.liip.ch'
    liipsync_fingerprints = [
        "69:7d:3e:eb:c1:c4:cc:90:a2:36:89:8a:a9:5a:13:5c",
        "2e:1a:d7:df:dd:b4:39:e7:af:d5:9f:ce:61:87:a7:ba"
    ]
    logger.info('Adding deploy key to digitalocean...')
    deploy_key_fingerprint = doctl_liip.add_ssh_key(
        key_name=f'{project_name_formatted}-dev-deploy-key',
        public_key=public_deploy_ssh_key
    )
    ssh_key_fingerprints = [personal_ssh_key_fingerprint, deploy_key_fingerprint] + liipsync_fingerprints
    logger.info(f'Creating droplet with name {project_name_formatted}-dev...')
    droplet_ip = doctl_liip.create_droplet(
        name=f'{project_name_formatted}-dev',
        size='s-1vcpu-1gb',
        ssh_keys=ssh_key_fingerprints,
    )
    logger.info('Adding project domain to digitalocean DNS...')
    doctl_liip.create_domain(
        domain=project_domain,
        ip_address=droplet_ip
    )
    logger.info(f'Adding wildcard record to {project_domain}...')
    doctl_liip.create_record(
        domain=project_domain,
        ip_address=droplet_ip,
        record_name="*",
        record_type="A"
    )

    return project_domain


def create_project_files(project_name):
    """
    Generates project files with given name from forge cookiecutter template

    :param project_name: Name of new project. Used to name new folders and variables
    """
    project_context = {
        "project_name": project_name,
        "project_prefix": project_name.lower().replace(' ', ''),
        "project_slug": project_name.lower().replace(' ', '-'),
        "django_secret_key_local": secrets.token_hex(100),
        "django_secret_key_staging": secrets.token_hex(100),
    }
    logger.info('Creating project files locally...')
    project_dir = cookiecutter(
        '..', output_dir='../../',
        extra_context=project_context,
        default_config=True,
        no_input=True
    )

    return project_dir


def create_gitlab_project(project_name: str, private_deploy_ssh_key: str, staging_domain: str):
    """
    Generates a gitlab project containing necessary configs to deploy to a DO droplet.

    :param project_name: Name of new gitlab project.
    :param private_deploy_ssh_key: Private component of deploy SSH key. Will be added as CI/CD variable.
        Public component must be added to droplets authorised keys
    :param staging_domain: Domain of droplet
    :returns project: Project object created by GitPython
    """
    logger.info('Creating gitlab project...')
    gl = gitlab.Gitlab.from_config('liip', ['/etc/python-gitlab.cfg'])
    amboss_group_id = gl.groups.list(search='amboss', top_level_only=True)[0].id
    project = gl.projects.create({'name': project_name, 'namespace_id': amboss_group_id})
    project.variables.create({'key': 'STAGING_DOMAIN', 'value': staging_domain})
    project.variables.create({'key': 'STAGING_SSH_PRIVATE_KEY', 'value': private_deploy_ssh_key})
    project.deploytokens.create({
        'name': 'gitlab-deploy-token',
        'scopes': ['read_registry', 'read_repository'],
        'username': '',
        'expires_at': ''
    })

    return project


def create_new_project(project_name: str, personal_ssh_key_fingerprint: str, local_only: bool=False):
    """
    Create a new forge project running on a digitalocean droplet hosted on gitlab with CI/CD.

    :param project_name: Name of project
    :param personal_ssh_key_fingerprint: SSH key fingerprint of personal SSH key on DO.
        This can be created/retreived from Settings -> Security on the DO dashboard
    :param local_only: If True, only create project files
    """
    summary = "\n"
    deploy_key = helpers.generate_deploy_ssh_key()
    project_dir = create_project_files(project_name)
    summary += f'Local project directory: {project_dir}\n'
    if not local_only:
        project_domain = create_do_resources(project_name, deploy_key['public'], personal_ssh_key_fingerprint)
        gitlab_project = create_gitlab_project(
            project_name,
            deploy_key['private'],
            staging_domain=f"{project_name.lower().replace(' ', '')}-dev.bedev.liip.ch"
        )
        logger.info('Pushing local files to git repository...')
        helpers.initialise_repo(gitlab_project.ssh_url_to_repo, project_dir)
        summary += f'Gitlab url: {gitlab_project.web_url}\n'
        summary += f'You can now SSH into your new droplet: ssh manager@{project_domain}\n'
        summary += f'NOTICE: Before you can deploy to your droplet you will need to copy the env file to it as ' \
                   f'follows:\n' \
                   f'ssh manager@{project_domain} "mkdir -p ~/srv/app/" \n' \
                   f'scp {project_dir}/.env.staging manager@{project_domain}:~/srv/app/.env'

    logger.info(summary)


if __name__ == "__main__":
    fire.Fire({
        'create_new_project': create_new_project,
        'create_gitlab_project': create_gitlab_project,
        'create_project_files': create_project_files,
        'create_do_resources': create_do_resources,
    })
