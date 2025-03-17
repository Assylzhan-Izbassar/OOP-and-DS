"""
Объект - понятие, которое имеет характеристику,
действия

Экземпляр объекта - объект с значениями
"""

# пример с столом
class Desk:
    """
    полями:
    длину, ширину, высоту, количество ног
    """
    # конструктор
    def __init__(self, length, width, height, num_legs):
        self.length = length
        self.width = width
        self.height = height
        self.num_legs = num_legs

    # методы - функции которые относятся данному классу

# экземпляр класса
white_desk = Desk(60, 50, 50, 4)

print("Высота данного стола =", white_desk.height)