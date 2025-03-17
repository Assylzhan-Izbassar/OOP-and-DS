from abc import ABC, abstractmethod


class Bottle(ABC):
    def __init__(self, bottle):
        self.bottle = bottle

    @abstractmethod
    def open(self):
        pass


class GlassBottle(Bottle):
    def __init__(self, bottle):
        super().__init__(bottle)

    def open(self):
        print('Открываем через открывашку')




class PlasticBottle(Bottle):
    def __init__(self, bottle):
        super().__init__(bottle)

    def open(self):
        print('Прокручиваем')


class BottleFactory:
    @staticmethod
    def generate_bottle(bottle_type: str):
        if bottle_type == 'glass':
            return GlassBottle(bottle_type)
        elif bottle_type == 'plastic':
            return PlasticBottle(bottle_type)
        else:
            print('Неизвестено')


gb = BottleFactory().generate_bottle('glass')
pb = BottleFactory().generate_bottle('plastic')

gb = GlassBottle()
pb = PlasticBottle()