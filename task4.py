# Процедурный код
n = 20
fibo = [0, 1]

for i in range(1, n+1):
    x = fibo[i] + fibo[i-1]
    fibo.append(x)

print(len(fibo))
print(fibo)


# В виде классов
class Fibonacci:
    def __init__(self, n): # конструктор
        self.n = n
        self.fibo = [0, 1]

        self.fill()

    def fill(self):
        for i in range(1, self.n+1):
            self.fibo.append(self.compute(i))

    def compute(self, x_i):
        return self.fibo[x_i] + self.fibo[x_i-1]


fibonacci = Fibonacci(20)
print(fibonacci.fibo[-1])