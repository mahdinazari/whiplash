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
    TYPES = {
        'Google': Google,
        'Github': Github,
        'Local': Local,
    }
    
    def __init__(self, type_, username, password):
        self.username = username
        self.password = password
        self.type_ = type_
        
    def create_object(self):
        if self.type_ not in LoginFactory.TYPES.keys():
            print('Invalid Type')
            return 
        
        obj = LoginFactory.TYPES[self.type_](self.username, self.password)
        return obj

login_factory = LoginFactory('Google', 'username', 'password').create_object()
login_factory.authenticate()
