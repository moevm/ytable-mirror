import os


class MetaSingleton(type):
    _instances = None

    def __call__(cls, *args, **kwargs):
        if cls._instances is None:
            cls._instances = super().__call__(*args, **kwargs)
        return cls._instances


class ConfigSingleton(metaclass=MetaSingleton):
    # Google
    G_SCOPES = ['https://www.googleapis.com/auth/drive']
    # create it your self
    G_SERVICE_ACCOUNT_FILE = None
    # Yandex
    Y_CLIENT_ID = '3542ffc72e2c4e9f8a1ff379081ed5a5'
    # go to https://oauth.yandex.ru/authorize?response_type=token&client_id=<Y_CLIENT_ID> and past received code here
    Y_OAuth = None

    def extend_from_confing_file(self, file="./config.txt"):
        assert os.path.isfile(file), "There is no config file found!"
        f = open(file, 'r').readlines()
        self.G_SERVICE_ACCOUNT_FILE = f[0][:-1]
        self.Y_OAuth = f[1][:-1]
