class Singleton(object):
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            print('Creating the object')
            cls._instance = super(Singleton, cls).__new__(cls)
 
        return cls._instance
       
       
obj1 = Singleton()
print(obj1)

obj2 = Singleton()
print(obj2)
