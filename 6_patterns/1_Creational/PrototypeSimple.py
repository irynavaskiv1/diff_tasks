import copy


class SSH:
    """
    purpose: add port 23 to prototype
    """

    def __init__(self, user: str, pwd: str, ip: str):
        self.user = user
        self.pwd = pwd
        self.ip = ip
        self.user = user
        self.connected = False
        self.port = 22

    def connect(self):
        self.connected = True

    def disconnect(self):
        self.connected = True


ssh1 = SSH(user='Ira', pwd='1234', ip='192.168.0.1')
ssh1.connect()

ssh2 = copy.deepcopy(ssh1)
ssh2.port = 23  # changed port without changing ssh1 port
