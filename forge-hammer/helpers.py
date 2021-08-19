from cryptography.hazmat.primitives import serialization as crypto_serialization
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.backends import default_backend as crypto_default_backend
from git import Repo


def generate_deploy_ssh_key():
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


def initialise_repo(git_url: str, project_dir: str):
    """
    Creates a git repo from the given folder and pushes it to the given git url.
    """
    repo = Repo.init(project_dir)
    repo.git.add(all=True)
    repo.index.commit("initial commit")
    remote = repo.create_remote('origin', url=git_url)
    remote.push(refspec='{}:{}'.format('master', 'master'))
    remote.push(refspec='{}:{}'.format('master', 'develop'))
