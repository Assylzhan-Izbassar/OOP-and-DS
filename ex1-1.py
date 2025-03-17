"""
Объекты - совокупность характеристик и дейстивий
Пример: объект студент
(имя, гпа, айдишка, курсы, мажор)
Нурым - он студент
"""

# ключевое слово - class
class Student:
    # параметр класса
    def __init__(self, name):
        self.name = name
        self.gpa = 0.0
        self.id = 0

student1 = Student('Нурым')
student1.name = 'Айбек'

print(student1.name)