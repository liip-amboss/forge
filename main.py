import fire
import logging
import doctl

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class Builder:
    """
    CLI used to build new forge applications
    """

    def create_project_server(self, project_name: str):
        """
        Create DO droplet running docker
        doctl compute droplet create --image docker-20-04 --size s-1vcpu-1gb --region fra1 test-doctl
        :param project_name: Name of project
        """
        doctl.compute.droplet.create(
            name=f'{project_name}-dev',
            image='docker-20-04',
            size='s-1vcpu-1gb',
            region='fra1'
        )

    def create_dns_entry(self, project_name: str):
        """
        Create DNS entry for new server
        :param project_name: Name of project
        """
        logger.info(f"Project name {project_name} ...")

    def create_project_repo(self, project_name: str):
        """
        Generates everything required for a new forge project including DO droplets and Gitlab projects
        :param project_name: Name of project
        """
        logger.info(f"Project name {project_name} ...")


if __name__ == "__main__":
    fire.Fire(Builder)
