import fire
import logging
import doctl
from cryptography.hazmat.primitives import serialization as crypto_serialization
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.backends import default_backend as crypto_default_backend

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class Builder:
    """
    CLI used to build new forge applications
    """

    def create_project_server(self, project_name: str, personal_ssh_key_fingerprint: str):
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

    def create_project_repo(self, project_name: str):
        """
        Generates everything required for a new forge project including DO droplets and Gitlab projects
        :param project_name: Name of project
        """
        logger.info(f"Project name {project_name} ...")


if __name__ == "__main__":
    fire.Fire(Builder)
