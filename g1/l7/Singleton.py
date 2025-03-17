class Singleton:
    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)

        return cls.__instance


class Logger(Singleton):
    def log(self, message):
        try:
            with open('log.txt', 'w') as log:
                log.write(message)
        except FileNotFoundError as e:
            print('Файл не найдет')



log = Logger()
log2 = Logger()
log.log('hello')
log.log('hello2')

print(log == log2)