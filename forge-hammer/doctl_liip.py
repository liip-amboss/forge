import subprocess


def create_droplet(name: str, size: str, ssh_keys: list):
    """
    Create Droplet and return its IP
    :param name: Name of droplet
    :param size: Droplet size
    :param ssh_keys: List of SSH key fingerprints to be added to the root user authorised keys.
    Keys must be added to DO first.
    """
    command = ['doctl', 'compute', 'droplet', 'create']
    args = [
        name,
        f'--size={size}',
        f'--ssh-keys={",".join(ssh_keys)}',
        '--image=docker-20-04',
        '--region=fra1',
        '--enable-monitoring=True',
        '--enable-private-networking=False',
        '--wait=True',
        '--user-data-file=createusers.sh',
        '--format=PublicIPv4'
    ]
    command.extend(args)

    process = subprocess.run(
        command,
        universal_newlines=True,
        stdout=subprocess.PIPE
    )
    droplet_ip = process.stdout.splitlines()[1]

    return droplet_ip


def create_domain(domain: str, ip_address):
    """
    Create DNS entry for new server
    :param project_name: Name of project
    :param ip_address: ip of droplet to connect to domain
    """
    command = ['doctl', 'compute', 'domain', 'create']
    args = [
        domain,
        f'--ip-address={ip_address}',
    ]
    command.extend(args)

    return subprocess.run(command)


def add_ssh_key(key_name: str, public_key: str):
    """
    Add SSH key to Digitalocean and return fingerprint
    :param project_prefix: Prefix of project
    :param public_key: Public key to be added to DO
    """
    command = ['doctl', 'compute', 'ssh-key', 'create']
    args = [
        key_name,
        f'--public-key={public_key}',
        '--format=FingerPrint',
    ]
    command.extend(args)
    process = subprocess.run(
        command,
        universal_newlines=True,
        stdout=subprocess.PIPE
    )
    fingerprint = process.stdout.splitlines()[1]

    return fingerprint

