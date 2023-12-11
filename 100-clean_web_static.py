#!/usr/bin/python3
# Fabfile to delete out-of-date archives.
import os
from fabric.api import *

env.hosts = ["104.196.168.90", "35.196.46.172"]

def do_clean(number=0):
    """Delete out-of-date archives.

    Args:
        number (int): The number of archives to keep.

    If number is 0 or 1, keeps only the most recent archive. If
    number is 2, keeps the most and second-most recent archives,
    etc.
    """
    number = max(1, int(number))

    # Local Cleanup
    local_versions_path = "versions"
    if not os.path.exists(local_versions_path):
        local("mkdir -p {}".format(local_versions_path))

    local_archives = sorted(os.listdir(local_versions_path))
    archives_to_delete_local = local_archives[:-number]
    [local("rm {}".format(os.path.join(local_versions_path, a))) for a in archives_to_delete_local]

    # Remote Cleanup
    with cd("/data/web_static/releases"):
        remote_archives = run("ls -tr").split()
        remote_archives = [a for a in remote_archives if "web_static_" in a]
        archives_to_delete_remote = remote_archives[:-number]
        [run("rm -rf ./{}".format(a)) for a in archives_to_delete_remote]
