from paramiko_expect import SSHClientInteraction

from paramiko_client import ParamikoClient


def test_channel():
    client = ParamikoClient('config.ini', 'PPM101')
    client.connect()
    interact = SSHClientInteraction(client.client, timeout=10, display=False)
    interact.expect(re_strings='.*#.*')
    interact.send('echo ""')
    interact.send('tail -f /opt/ppm/ppm/QX_DEV_OPS_962/server/kintana/log/serverLog.txt')
    interact.tail(output_callback=lambda m: output_callback(m, interact), stop_callback=lambda x: get_is_stop(x), timeout=100)


def output_callback(line, interact):
    if 'exit#@#' in line:
        interact.send("exit-------- ")
    else:
        print(line)


def get_is_stop(line):
    # print(line)
    pass


test_channel()
