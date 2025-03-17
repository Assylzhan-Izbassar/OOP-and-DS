from abc import ABC, abstractmethod

class Storage(ABC):
    @abstractmethod
    def save(self, filename, content):
        pass

    @abstractmethod
    def load(self, filename):
        pass

class FileStorage(Storage):
    def save(self, filename, content):
        try:
            with open(filename, 'wb') as file:
                file.write(content)
        except Exception as e:
            print(e)


    def load(self, filename):
        try:
            with open(filename, 'r') as file:
                return file.read()
        except FileNotFoundError as e:
            return 'File not found'


fs = FileStorage()
print(fs.load('test.txt'))
print(fs.save('test.txt', 'Hello World!'))

print('Our program is finished.')