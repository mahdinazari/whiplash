import types


class CopyStrategy:
    def __init__(self, source_path, destination_path, func=None):
        self.name = 'None in func Strategy'
        self.source_path = source_path
        self.destination_path = destination_path
        if func is not None:
            self.execute = types.MethodType(func, self)

    def execute(self):
        print(self.name)

    def regular_copy(self):
        print(self.name + ' from execute object1')
        print(f'Copy Files From {self.source_path} To {self.destination_path}')

    def zip_copy(self):
        print(self.name + ' from execute object2')
        print(f'Copy ZIP Files From {self.source_path} To {self.destination_path}')


if __name__ == '__main__':
    obj1 = CopyStrategy('/mnt/input/', '/mnt/output/output_directory', regular_copy)
    obj1.name = 'Reqular Copy Strategy'
   
    obj2 = CopyStrategy('/mnt/input/', '/mnt/output/zip_file.zip', zip_copy)
    obj2.name = 'Zip Copy Strategy'
   
    obj1.execute()
    obj2.execute()

