#!/usr/bin/python3
"""Fabric script to generate .tgz archive"""
# from the contents of the web_static folder of AirBnB Clone repo

from fabric.api import local, env
from datetime import datetime

env.user = 'ubuntu'
env.hosts = ['44.200.74.227' '18.232.49.201']


def do_pack():
    '''generates .tgz archive from the contents of the web_static folder'''
    now = datetime.now().strftime("%Y%m%d%H%M%S")
    local('sudo mkdir -p ./versions')
    path = './versions/web_static_{}'.format(now)
    local('sudo tar -czvf {}.tgz web_static'.format(path))
    name = '{}.tgz web_ststic'.format(path)
    if name:
        return name
    else:
        return None
