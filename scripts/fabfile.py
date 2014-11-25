from fabric.api import sudo, local, env
from fabric.colors import green

env.hosts = ['localhost']


def prepare_env():
    print(green("Installing base linux packages"))
    sudo("apt-get install -y python-dev python-virtualenv virtualenvwrapper")


def install_env():
    print(green("Starting install"))
    print(green("Installing python packages..."))
    # In this local command we use shell arg for keep the current virtualenv in command
    local("pip install -r requirements.txt", shell='/bin/bash')
    print(green("Python packages installed"))
    print(green("You can now run the project"))
