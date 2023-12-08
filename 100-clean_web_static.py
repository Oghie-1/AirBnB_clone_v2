#!/usr/bin/env python3
"""
Fabric script to delete out-of-date archives
"""

from fabric.api import local, run, env, lcd
from datetime import datetime
import os

env.hosts = ['<IP web-01>', '<IP web-02>']
env.user = '<your_username>'
env.key_filename = '<path_to_your_private_key>'

def do_clean(number=0):
    """
    Deletes out-of-date archives
    """
    number = int(number)
    if number < 0:
        return

    """Delete local archives"""
    local_archives = sorted(os.listdir('versions'))
    archives_to_delete_local = local_archives[:-number] if number > 1 else local_archives[:-1]
    with lcd('versions'):
        for archive in archives_to_delete_local:
            local('rm -f {}'.format(archive))

    """Delete remote archives"""
    run_archives = run('ls -1 /data/web_static/releases/')
    remote_archives = run_archives.split()
    archives_to_delete_remote = sorted(remote_archives)[:-number] if number > 1 else sorted(remote_archives)[:-1]
    for archive in archives_to_delete_remote:
        run('rm -f /data/web_static/releases/{}'.format(archive))

if __name__ == '__main__':
    do_clean(2)
