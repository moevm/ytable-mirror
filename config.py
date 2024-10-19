class MetaSingleton(type):
    _instances = None

    def __call__(cls, *args, **kwargs):
        if cls._instances is None:
            cls._instances = super().__call__(*args, **kwargs)
        return cls._instances


class ConfigSingleton(metaclass=MetaSingleton):
    # Google
    G_SCOPES = ['https://www.googleapis.com/auth/drive']
    G_SERVICE_ACCOUNT_FILE = './sheetsconverter-438022-dbe9934c7a3b.json'
    # Yandex
    Y_CLIENT_ID = '3542ffc72e2c4e9f8a1ff379081ed5a5'
    # go to https://oauth.yandex.ru/authorize?response_type=token&client_id=<Y_CLIENT_ID> and past received code here
    Y_OAuth = ""
