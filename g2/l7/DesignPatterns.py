from abc import ABC, abstractmethod

class Button(ABC):
    @abstractmethod
    def render(self):
        pass


class WindowsButton(Button):
    def render(self):
        print('Windows Button')


class MacOSButton(Button):
    def render(self):
        print('MacOS Button')


class ButtonFactory:
    @staticmethod
    def create_button(type_os: str):
        if type_os == 'WindowsButton':
            return WindowsButton()
        elif type_os == 'MacOSButton':
            return MacOSButton()
        else:
            return None

button_factory = ButtonFactory()

wb = button_factory.create_button('WindowsButton')
mb = button_factory.create_button('MacOSButton')

wb2 = WindowsButton()
mb2 = MacOSButton()




class Singleton:
    _instances = None

    def __new__(cls):
        if cls._instances is None:
            cls._instances = super().__new__(cls)
        return cls._instances

class Logger(Singleton):
    def log(self, message):
        print(message)

logger = Logger()
logger2 = Logger()

print(logger == logger2)