import doctl


def create_droplet(name: str, size: str, ssh_keys: list):
    return doctl.compute.droplet.create(
        name=name,
        image='docker-20-04',
        size=size,
        region='fra1',
        enable_monitoring=True,
        enable_private_networking=False,
        ssh_keys=ssh_keys,
        wait=True
    )


def create_domain(domain: str, ip_address):
    """
    Create DNS entry for new server
    :param project_name: Name of project
    :param ip_address: ip of droplet to connect to domain
    """
    doctl.compute.domain.create(
        domain=domain,
        ip_address=ip_address
    )


def add_ssh_key(key_name: str, public_key: str):
    """
    Add SSH key to Digitalocean and return fingerprint
    :param project_prefix: Prefix of project
    :param public_key: Public key to be added to DO
    """
    response = doctl.compute.ssh_key.create(
        key_name=key_name,
        public_key=public_key,
    )

    return response[0]['fingerprint']


def get_droplet_ip_from_id(droplet_id: int):
    """
    Return IP of given droplet ID
    :param droplet_id: Name of project
    """
    droplet = doctl.compute.droplet.get(str(droplet_id))

    return droplet[0]['networks']['v4'][1]['ip_address']