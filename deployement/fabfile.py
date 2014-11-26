from fabric.api import sudo, cd, run
from fabric.colors import green, yellow
import ConfigParser


def install_api_serveur(conf_file):
    config = ConfigParser.ConfigParser()
    config.read(conf_file)
    print(yellow("Warning : You need to execute this script with sudoer"))
    print(green("Installing linux packages..."))
    sudo("apt-get install -y nginx supervisort python-dev python-virtualenv")
    print(green("Linux packages installed"))
    print(green("Creating project path"))
    api_path = config.get('Global', 'api_path')
    sudo("mkdir {0}".format(api_path))
    with cd(api_path):
        run("virtualenv ics2web")
    print(green("setting up virtualenv"))
    source = "source {0} && ".format(api_path + "ics2web")
    print(green("Installing requirements for project"))
    run(source + "pip install -r " + api_path + "/scripts/requirements.txt")
    run(source + "pip install gunicorn")
    print(green("Configuring gunicorn"))
    with open(config.get('Files', 'gunicorn_template')) as f:
        content = f.read()
        content = content.format(api_path, config.get('Global', 'user'),
                                 config.get('Global', 'group'),
                                 config.get('Global', 'workders'))
        run('echo "{0}" > {1}'.format(content, api_path + '/ics2web/run/gunicorn_start'))
        run('chmod a+x ' + api_path + '/ics2web/run/gunicorn_start')
    print(green("Configuring nginx"))
    with open(config.get('Files', 'nginx_template')) as f:
        content = f.read()
        content = content.format(api_path, config.get('Nginx', 'access_log'),
                                 config.get('Nginx', 'error_log'),
                                 config.get('Nginx', 'server_name'))
        sudo('echo "{0}" > {1}'.format(content, '/etc/nginx/sites-available/ics2web'))
        sudo("ln -s /etc/nginx/sites-available/ics2web /etc/nginx/sites-enabled/ics2web")
        sudo('service nginx restart')
    print(green("Configuring supervisor"))
    with open(config.get('Files', 'supervisor_template')) as f:
        content = f.read()
        content = content.format(api_path,
                                 config.get('Global', 'user'),
                                 config.get('Global', 'group'),
                                 config.get('Supervisor', 'log_file'))
        sudo('echo "{0}" > {1}'.format(content, '/etc/supervisor/conf.d/ics2web.conf'))
    print(green("Starting application"))
    sudo('supervisorctl start ics2web')
