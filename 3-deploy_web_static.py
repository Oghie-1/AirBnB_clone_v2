#!/usr/bin/python3
# Fabfile to create and distribute an archive to a web server.
import os.path
from datetime import datetime
from fabric.api import env, local, put, run

env.hosts = ["104.196.168.90", "35.196.46.172"]

def do_pack():
    """Create a tar gzipped archive of the directory web_static."""
    dt = datetime.utcnow().strftime("%Y%m%d%H%M%S")
    file = os.path.join("versions", "web_static_{}.tgz".format(dt))
    
    if not os.path.exists("versions"):
        local("mkdir -p versions")

    with lcd("web_static"):
        local("tar -cvzf {} .".format(file))

    return file if os.path.isfile(file) else None

def do_deploy(archive_path):
    """Distribute an archive to a web server."""
    if not os.path.isfile(archive_path):
        return False

    file = os.path.basename(archive_path)
    name = file.split(".")[0]

    if put(archive_path, "/tmp/{}".format(file)).failed:
        return False

    commands = [
        "rm -rf /data/web_static/releases/{}/".format(name),
        "mkdir -p /data/web_static/releases/{}/".format(name),
        "tar -xzf /tmp/{} -C /data/web_static/releases/{}/".format(file, name),
        "rm /tmp/{}".format(file),
        "mv /data/web_static/releases/{}/web_static/* /data/web_static/releases/{}/".format(name, name),
        "rm -rf /data/web_static/releases/{}/web_static".format(name),
        "rm -rf /data/web_static/current",
        "ln -s /data/web_static/releases/{}/ /data/web_static/current".format(name)
    ]

    for command in commands:
        if run(command).failed:
            return False

    return True

def deploy():
    """Create and distribute an archive to a web server."""
    file = do_pack()
    if file is None:
        return False
    return do_deploy(file)
