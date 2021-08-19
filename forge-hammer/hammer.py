import secrets
import fire
import logging
import doctl_liip
import helpers
import gitlab
from git import Repo
from cookiecutter.main import cookiecutter


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class Builder:
    """
    CLI used to build new forge applications
    """

    def create_new_project(self, project_name: str, personal_ssh_key_fingerprint: str, local_only: bool=False):
        """
        Create a new forge project running on a digitalocean droplet hosted on gitlab with CI/CD.
        :param project_name: Name of project
        :param personal_ssh_key_fingerprint: SSH key fingerprint of personal SSH key on DO
        :param local_only: If True, only create project files
        """
        summary = ""
        deploy_key = helpers.generate_deploy_ssh_key()
        project_dir = self.create_project_files(project_name)
        summary += f'Local project directory: {project_dir}\n'
        if not local_only:
            project_domain = self.create_do_resources(project_name, deploy_key['public'], personal_ssh_key_fingerprint)
            gitlab_project = self.create_gitlab_project(
                project_name,
                deploy_key['private'],
                staging_domain=f"{project_name.lower().replace(' ', '')}-dev.bedev.liip.ch"
            )
            self.initialise_repo(gitlab_project.ssh_url_to_repo, project_dir)
            summary += f'Gitlab url: {gitlab_project.web_url}\n'
            summary += f'You can now SSH into your new droplet: ssh@{project_domain}'

        logger.info(summary)

    def create_do_resources(self, project_name: str, public_deploy_ssh_key: str, personal_ssh_key_fingerprint: str):
        """
        Create DO resources required for a new project. Droplet, Domain, SSH keys
        :param project_name: Name of project
        :param public_deploy_ssh_key: Public deploy ssh key to be added to droplet
        :param personal_ssh_key_fingerprint: SSH key fingerprint of personal SSH key on DO
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

        return project_domain

    def create_project_files(self, project_name):
        """
        Generates project with given name from forge cookiecutter template
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

    def create_gitlab_project(self, project_name: str, private_deploy_ssh_key: str, staging_domain: str):
        """
        Generates a gitlab project containing the droplets domain and the private deploy ssh key.
        :param project_name: Name of new gitlab project.
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

    def initialise_repo(self, git_url, project_dir):
        """
        Creates a git repo from the given folder and pushes it to the given git url.
        """
        logger.info('Pushing local files to git repository...')
        repo = Repo.init(project_dir)
        repo.git.add(all=True)
        repo.index.commit("initial commit")
        remote = repo.create_remote('origin', url=git_url)
        remote.push(refspec='{}:{}'.format('master', 'master'))
        remote.push(refspec='{}:{}'.format('master', 'develop'))


if __name__ == "__main__":
    fire.Fire(Builder)
