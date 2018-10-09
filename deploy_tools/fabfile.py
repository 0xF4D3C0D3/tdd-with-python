import os
import random


from fabric.contrib.files import append, exists
from fabric.api import cd, env, local, run, settings

env.user = 'elspeth'
env.key_filename = os.path.expanduser('~/.ssh/digital-ocean')


REPO_URL = 'https://github.com/0xB4DF4C3D/tdd-with-python'


def _get_latest_source():
    if exists('.git'):
        run('git fetch')
    else:
        run(f'git clone {REPO_URL} .')
    current_commit = local('git log -n 1 --format=%H', capture=True)
    run(f'git reset --hard {current_commit}')


def _update_virtualenv():
    if not exists('virtualenv/bin/pip'):
        run(f'python3.6 -m venv virtualenv')
    run('./virtualenv/bin/pip install -r requirements.txt')




def deploy():
    site_folder = f'/home/{env.user}/sites/{env.host}'
    run(f'mkdir -p {site_folder}')
    with cd(site_folder):
        _get_latest_source()
        run('pwd')
