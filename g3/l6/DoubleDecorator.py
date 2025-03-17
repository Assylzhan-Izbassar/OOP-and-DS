import time

def func(nums):
    def decorator(func):
        def wrapper():
            print('Вызов')
            for _ in range(nums):
                func()

        return wrapper
    return decorator

@func(3)
def say_hello():
    print("Hello World!")

# @func(10)
# def time():
#     print(1)

# time()


### 2 пример - Измерить время
def time_it(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        func(args[0])
        end_time = time.time()

        delta_time = end_time - start_time

        print('Время выполнение данной функции', delta_time, 'сек')

    return wrapper

@time_it
def algos():
    time.sleep(2)
    print('Результат')

@time_it
def sum(n):
    res = 0
    for i in range(n):
        res += i
    print(res)


start_time = time.time()
# algos()
end_time = time.time()


start_time = time.time()
# sum(100)
end_time = time.time()

def log(prefix):
    def decorator(cls):
        add_method = cls.add

        def wrapper(self, *args, **kwargs):
            print(f'{prefix}: вызов {add_method.__name__} с {args}')
            return add_method(self, *args, **kwargs)
        cls.add = wrapper
        return cls
    return decorator


@log('INFO')
class MathOperations:
    def add(self, a, b):
        return a + b

m = MathOperations()
print(m.add(3, 4))


def property2(func):
    def wrapper():
        print('декоратор')
        return func()

    return wrapper

_a = 5

@property2
def a():
    return _a


# def a(value):
#     _a = value
#
# print(a())
# print(a(50))
# print(a())


