from fabric.api import sudo, cd, run, env
from fabric.colors import green, yellow
from fabric.contrib.files import append
import ConfigParser

env.hosts = ['10.104.10.63']


def install_api_server(conf_file):
    config = ConfigParser.ConfigParser()
    config.read(conf_file)
    api_path = config.get('Global', 'api_path')
    print(yellow("Warning : You need to execute this script with sudoer"))
    print(green("Installing linux packages..."))
    sudo("apt-get install -y nginx supervisor python-dev python-virtualenv git")
    print(green("Linux packages installed"))
    print(green("Creating project path"))
    run("git clone https://karec@bitbucket.org/karec/ics2web.git {0}".format(api_path))
    with cd(api_path):
        run("virtualenv ics2web")
    print(green("setting up virtualenv"))
    source = "source {0} && ".format(api_path + "/ics2web/bin/activate")
    print(green("Installing requirements for project"))
    run(source + "pip install -r " + api_path + "/scripts/requirements.txt")
    run(source + "pip install gunicorn")
    print(green("Configuring gunicorn"))
    with open(config.get('Files', 'gunicorn_template')) as f:
        content = f.read()
        content = content.format(api_path, config.get('Global', 'user'),
                                 config.get('Global', 'group'),
                                 config.getint('Global', 'workers'))
        run('touch {0}'.format(api_path + '/ics2web/bin/gunicorn_start'))
        append(api_path + '/ics2web/bin/gunicorn_start', content, escape=True)
        run('chmod a+x ' + api_path + '/ics2web/bin/gunicorn_start')
    print(green("Configuring nginx"))
    with open(config.get('Files', 'nginx_template')) as f:
        content = f.read()
        content = content.format(api_path, config.get('Nginx', 'access_log'),
                                 config.get('Nginx', 'error_log'),
                                 config.get('Nginx', 'server_name'))
        sudo("touch {0}".format("/etc/nginx/sites-available/ics2web"))
        append('/etc/nginx/sites-available/ics2web', content, use_sudo=True)
        sudo("ln -s /etc/nginx/sites-available/ics2web /etc/nginx/sites-enabled/ics2web")
        sudo('service nginx restart')
    print(green("Configuring supervisor"))
    with open(config.get('Files', 'supervisor_template')) as f:
        content = f.read()
        content = content.format(api_path,
                                 config.get('Global', 'user'),
                                 config.get('Global', 'group'),
                                 config.get('Supervisor', 'log_file'))
        sudo("touch {0}".format("/etc/supervisor/conf.d/ics2web.conf"))
        append('/etc/supervisor/conf.d/ics2web.conf', content, use_sudo=True)
        sudo('supervisorctl reload')
    print(green("Starting application"))
    sudo('supervisorctl start ics2web')
