import fire
import logging
import doctl
import gitlab
from git import Repo
from cookiecutter.main import cookiecutter
from cryptography.hazmat.primitives import serialization as crypto_serialization
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.backends import default_backend as crypto_default_backend

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class Builder:
    """
    CLI used to build new forge applications
    """

    def create_project(self, project_name: str, personal_ssh_key_fingerprint: str):
        """
        Create DO droplet running docker
        :param project_name: Name of project
        :param personal_ssh_key_fingerprint: SSH key fingerprint of personal SSH key on DO
        """
        deploy_key = self.generate_deploy_ssh_key()
        deploy_key_fingerprint = self.add_ssh_key_to_do(project_name=project_name, public_key=deploy_key['public'])
        droplet = doctl.compute.droplet.create(
            name=f'{project_name}-dev',
            image='docker-20-04',
            size='s-1vcpu-1gb',
            region='fra1',
            enable_monitoring=True,
            enable_private_networking=False,
            ssh_keys=[personal_ssh_key_fingerprint, deploy_key_fingerprint],
            wait=True
        )
        droplet_id = droplet[0]['id']
        server_ip = self.get_droplet_ip(droplet_id)
        self.create_domain(project_name=project_name, ip_address=server_ip)
        project_dir = self.create_project_folder()
        git_ssh_url = self.create_gitlab_repo(project_name=project_name, deploy_ssh_key=deploy_key['private'])
        self.push_project(git_url=git_ssh_url, project_dir=project_dir)

    def create_domain(self, project_name: str, ip_address):
        """
        Create DNS entry for new server
        :param project_name: Name of project
        :param ip_address: ip of droplet to connect to domain
        """
        doctl.compute.domain.create(
            domain=f'{project_name}-dev.bedev.liip.ch',
            ip_address=ip_address
        )

    def add_ssh_key_to_do(self, project_name: str, public_key: str):
        """
        Add SSH key to Digitalocean and return fingerprint
        :param project_name: Name of project
        :param public_key: Public key to be added to DO
        """
        response = doctl.compute.ssh_key.create(
            key_name=f'{project_name}-dev-deploy-key',
            public_key=public_key,
        )

        return response[0]['fingerprint']

    def generate_deploy_ssh_key(self):
        """
        Create SSH key to be used by gitlab to deploy
        """

        key = rsa.generate_private_key(
            backend=crypto_default_backend(),
            public_exponent=65537,
            key_size=2048
        )
        private_key = key.private_bytes(
            crypto_serialization.Encoding.PEM,
            crypto_serialization.PrivateFormat.PKCS8,
            crypto_serialization.NoEncryption())
        public_key = key.public_key().public_bytes(
            crypto_serialization.Encoding.OpenSSH,
            crypto_serialization.PublicFormat.OpenSSH
        )

        return {'public': public_key.decode('utf-8'), 'private': private_key.decode('utf-8')}

    def get_droplet_ip(self, droplet_id: int):
        """
        Return IP of given droplet ID
        :param droplet_id: Name of project
        """
        droplet = doctl.compute.droplet.get(str(droplet_id))

        return droplet[0]['networks']['v4'][1]['ip_address']

    def create_project_folder(self):
        """
        Generates project with given name from cookiecutter template
        """
        project_dir = cookiecutter('.', output_dir='../')
        return project_dir

    def create_gitlab_repo(self, project_name, deploy_ssh_key):
        """
        Generates project with given name from cookiecutter template
        """
        gl = gitlab.Gitlab.from_config('liip', ['/etc/python-gitlab.cfg'])
        group_id = gl.groups.list(search='amboss')[0].id
        project = gl.projects.create({'name': project_name, 'namespace_id': group_id})
        project.variables.create({'key': 'STAGING_DOMAIN', 'value': f'{project_name}-dev.bedev.liip.ch'})
        project.variables.create({'key': 'STAGING_SSH_PRIVATE_KEY', 'value': deploy_ssh_key})
        project.deploytokens.create({
            'name': 'gitlab-deploy-token',
            'scopes': ['read_registry', 'read_repository'],
            'username': '',
            'expires_at': ''
        })

        return project.ssh_url_to_repo

    def push_project(self, git_url, project_dir):
        repo = Repo.init(project_dir)
        repo.git.add(all=True)
        repo.index.commit("initial commit")
        remote = repo.create_remote('origin', url=git_url)
        remote.push(refspec='{}:{}'.format('master', 'origin/master'))


if __name__ == "__main__":
    fire.Fire(Builder)
