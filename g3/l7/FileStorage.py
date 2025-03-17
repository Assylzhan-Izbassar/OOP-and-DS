from abc import ABC, abstractmethod


class Storage(ABC): # interface
    @abstractmethod
    def save(self, content):
        pass

    @abstractmethod
    def load(self, filename):
        pass


class FileStorage(Storage):
    def load(self, filename: str) -> str:
        try:
            with open(filename, 'r') as file:
                return file.read()
        except FileNotFoundError as error:
            return 'File not found'

    def save(self, content: str) -> None:
        with open('data.txt', 'w') as file:
            file.write(content)

# storage = Storage()
# print(storage)
# print(storage.save('hello!'))

fs = FileStorage()
fs.save('Hello!')
msg = fs.load('data2txt')
print(msg)

print('Application is finished!')