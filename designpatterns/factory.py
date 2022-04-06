from abc import abstractmethod, ABCMeta


class ILogin:
    __metaclass__ = ABCMeta

    def __init__(self, username, password):
        self.username = username
        self.password = password

    @abstractmethod
    def authenticate(self):
        raise NotImplementedError


class Github(ILogin):
    def authenticate(self):
        print('request to github')
        print('authenticate with github')


class Google(ILogin):
    def authenticate(self):
        print('request to google')
        print('authenticate with google')


class Local(ILogin):
    def authenticate(self):
        print('request to local')
        print('authenticate with local')


class LoginFactory:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def create_object(self, type_):
        obj = eval(type_)(self.username, self.password)
        return obj

login_factory = LoginFactory('username', 'password')
login_factory.create_object('Google').authenticate()
