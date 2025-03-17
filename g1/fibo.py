"""
Напишите программу Python, которая выводит первые 20 чисел
последовательности Фибоначчи с помощью цикла for.
"""

# f_0 = 0
# f_1 = 1
# f_2 = 1
# f_i = f_i-1 + f_i-2

"""
Процедурный код
"""
n = 20
fibo = [0, 1]

for i in range(2, n + 1):
    fibo.append(fibo[i - 1] + fibo[i-2])

for i in range(len(fibo)):
    print(fibo[i], i)

"""
Объетно-ориентированный подход
"""
class Fibo:
    # инициализируем поля
    def __init__(self, n): # конструктор
        self.n = n
        self.fibo = [0, 1]
        self.fill_fibo()

    # методы
    def fill_fibo(self):
        for i in range(2, n + 1):
            self.fibo.append(self.calculate(i))

    def calculate(self, i):
        return self.fibo[i - 1] - self.fibo[i - 2]

    def get_last_fibo(self):
        return self.fibo[-1]


fibo_20 = Fibo(20)
print(fibo_20.get_last_fibo())