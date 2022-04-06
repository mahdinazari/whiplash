class User:
    def __init__(self, name, age):
        self.name = name
        self.__age = None
        self.age = age
 
    @property
    def age(self):
        return self.__age
    
    @age.setter
    def age(self, value):
        if value <= 0 or value > 99:
            self.__age = 0
            print('Wrong age in input')
            return
        
        self.__age = value
        print(f'Age days is {self.__age * 365}')


if __name__ == '__main__':
    user = User('mehdi', -30)
    print(user.name)
    print(user.age)
    