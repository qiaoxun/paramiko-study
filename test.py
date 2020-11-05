# import paramiko
#
# client = paramiko.SSHClient()
# # client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
# client.load_system_host_keys()
# client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
# client.connect(hostname='192.168.56.101', port=22, username='root', password='root', timeout=1)
# stdin, stdout, stderr = client.exec_command('cat /home/joey/study/devops/mysql/private_key.pem')
# for line in stdout:
#     print(line)
#

from paramiko_client import ParamikoClient

# if __name__ == '__main__':
#     client = ParamikoClient('config.ini')
#     client.connect()
#     client.run_command('cat /home/joey/study/devops/mysql/private_key.pem')
#     client.run_command('echo $PATH')


# def upload_file():
#     client = ParamikoClient('config.ini')
#     # client.connect()
#     sftp_client = client.get_sftp_client()
#     sftp_client.put('C:/Users/qiaox.CORPDOM/Desktop/sys_roles_menus.sql', '/home/joey/aaa.sql')
#     client.run_command('ls /home/joey')
#
#
# upload_file()


# def start_django_project():
#     client = ParamikoClient('config.ini')
#     client.connect()
#     client.run_command('source /home/joey/study/django/python38env/bin/activate && cd /media/sf_dev-ops/rest_xops && python manage.py runserver 0:8003 2>&1')
#
# start_django_project()


def connect_to_101():
    client = ParamikoClient('config.ini', 'PPM101')
    client.connect()
    home = "/opt/ppm/ppm/"
    # file = '/opt/ppm/ppm/QX_DEV_OPS_962_1/ppm962/test/install.log'
    # cmd = 'file=' + file + '&&mkdir -p "${file%/*}" && touch "$file"'
    _, stdout, _ = client.run_command("cd /opt/ppm/ppm/ && for i in $(ls -d */); do echo ${i}; done")

    for line in iter(stdout.readline, ""):
        print(line.strip())
        if is_ppm_instance(home, line.strip(), client):
            print("it's PPM instance")


def is_ppm_instance(home, folder, client):
    command = "cd " + home + folder + " && ls -l | grep server.conf | wc -l"
    _, stdout, _ = client.run_command(command)
    for count in iter(stdout.readline, ""):
        if int(count) > 0:
            # read_server_conf_file(home, folder, client)
            # is_ppm_running(home, folder, client)
            get_ppm_version(home, folder, client)
    return False


def read_server_conf_file(home, folder, client):
    command = "cat " + home + folder + "server.conf"
    _, stdout, _ = client.run_command(command)
    try:
        for line in iter(stdout.readline, ""):
            if "com.kintana.core.server.BASE_URL" in line:
                print(line)
    except Exception:
        print("Unexpected error")


def is_ppm_running(home, folder, client):
    command = "ps -ef | grep " + home + folder + " | grep -v grep | wc -l"
    _, stdout, _ = client.run_command(command)
    for count in iter(stdout.readline, ""):
        if int(count) > 0:
            print(folder + "is running")


def get_ppm_version(home, folder, client):
    command = "head " + home + folder + "conf/version.txt"
    _, stdout, _ = client.run_command(command)
    version = ""
    for line in iter(stdout.readline, ""):
        if len(version) > 0:
            break
        version = line.strip()
    return version


connect_to_101()


