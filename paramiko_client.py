import paramiko
import configparser


class ParamikoClient(object):

    def __init__(self, config_file):
        config = configparser.ConfigParser()
        config.read(config_file)
        self.host = config.get('ssh', 'host')
        self.port = int(config.get('ssh', 'port'))
        self.username = config.get('ssh', 'username')
        self.password = config.get('ssh', 'password')
        self.timeout = float(config.get('ssh', 'timeout'))
        self.client = paramiko.SSHClient()
        self.client_connected = 0
        self.sftp_client = None
        # self.client.load_system_host_keys()
        self.client.set_missing_host_key_policy(paramiko.WarningPolicy())
        print(self.client)

    def connect(self):
        try:
            self.client.connect(hostname=self.host, port=self.port, username=self.username, password=self.password, timeout=self.timeout)
            self.client_connected = 1
        except Exception as e:
            print(e)
            try:
                self.client.close()
            except:
                pass

    def run_command(self, cmd_str):
        stdin, stdout, stderr = self.client.exec_command(cmd_str, get_pty=True)
        while True:
            next_line = stdout.readline().strip()  # 读取脚本输出内容
            print('line: ' + next_line)
            if next_line == 'Quit the server with CONTROL-C.':
                break

    def get_sftp_client(self):
        if self.client_connected == 0:
            self.connect()
        if not self.sftp_client:
            self.sftp_client = paramiko.SFTPClient.from_transport(self.client.get_transport())
        return self.sftp_client
