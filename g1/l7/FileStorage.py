from abc import ABC, abstractmethod

class Storage(ABC):
    @abstractmethod
    def save(self, filename, content):
        pass

    @abstractmethod
    def load(self, filename):
        pass


class FileStorage(Storage):
    def load(self, filename):
        try:
            with open(filename, 'r') as file:
                return file.read()
        except FileNotFoundError as e:
            print('Файл не найден', e)
            return None

    def save(self, filename, content):
        try:
            with open(filename, 'w') as file:
                file.write(content)
        except FileNotFoundError as e:
            print('Файл не найден. Мы не можем записать')


fs = FileStorage()
data = fs.load('data.txt') if fs.load('data.txt') is not None else 'Нету файла'

print(data)

print('Завершеаем программу')

fs.save('data.txt', 'Мир во всем мире')