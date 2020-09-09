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
        self.client.load_system_host_keys()
        self.client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        print(self.client)

    def connect(self):
        try:
            self.client.connect(hostname=self.host, port=self.port, username=self.username, password=self.password, timeout=self.timeout)
        except Exception as e:
            print(e)
            try:
                self.client.close()
            except:
                pass

    def run_command(self, cmd_str):
        stdin, stdout, stderr = self.client.exec_command(cmd_str)
        for line in stdout:
            print(line)

