class House:
    root = 'beton'
    def __init__(self, color, rooms): # конструктор
        self.color = color
        self.__rooms = rooms

    # getter
    def get_rooms(self):
        return self.__rooms

    # setter
    def set_rooms(self, rooms):
        if rooms > 0: # валидация
            self.__rooms = rooms
        else:
            print('Количество комнат должно быть больше 0')

house1 = House('red', 3)
print(house1.color)
print(house1.get_rooms())

house1.set_rooms(4)

print(house1.get_rooms())