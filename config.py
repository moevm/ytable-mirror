class MetaSingleton(type):
    _instances = None

    def __call__(cls, *args, **kwargs):
        if cls._instances is None:
            cls._instances = super().__call__(*args, **kwargs)
        return cls._instances


class ConfigSingleton(metaclass=MetaSingleton):
    # Google
    G_SCOPES = ['https://www.googleapis.com/auth/drive']
    G_SERVICE_ACCOUNT_FILE = './GoogleCloud/sheetsconverter-438022-dbe9934c7a3b.json'
    # Yandex
    Y_OAuth = "y0_AgAAAABpmRHMAAyYtAAAAAEUIT4rAAA9-BucjP1BArrFAuAKsxVIiw6iwA"
