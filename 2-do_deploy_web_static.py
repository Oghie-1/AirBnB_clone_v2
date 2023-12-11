#!/usr/bin/python3
# Fabfile to distribute an archive to a web server.
import os.path
from fabric.api import env, put, run


env.hosts = ["104.196.168.90", "35.196.46.172"]

def do_deploy(archive_path):
    """Distributes an archive to a web server.

    Args:
        archive_path (str): The local path of the archive to distribute.

    Returns:
        bool: True if the deployment is successful, False otherwise.
    """
    if not os.path.isfile(archive_path):
        return False

    file = os.path.basename(archive_path)
    name = file.split(".")[0]

    # Upload archive to /tmp directory on the remote server
    if put(archive_path, f"/tmp/{file}").failed:
        return False

    # Create necessary directories and extract the archive
    commands = [
        f"rm -rf /data/web_static/releases/{name}/",
        f"mkdir -p /data/web_static/releases/{name}/",
        f"tar -xzf /tmp/{file} -C /data/web_static/releases/{name}/",
        f"rm /tmp/{file}",
        f"mv /data/web_static/releases/{name}/web_static/* /data/web_static/releases/{name}/",
        f"rm -rf /data/web_static/releases/{name}/web_static",
        f"rm -rf /data/web_static/current",
        f"ln -s /data/web_static/releases/{name}/ /data/web_static/current",
    ]

    # Execute the commands on the remote server and check for failures
    for command in commands:
        if run(command).failed:
            return False

    return True
