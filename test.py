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


def upload_file():
    client = ParamikoClient('config.ini')
    client.connect()
    sftp_client = client.get_sftp_client()
    sftp_client.put('C:/Users/qiaox.CORPDOM/Desktop/Script/test.s    h', '/home/joey')
    client.run_command('ls /home/joey')

upload_file()
