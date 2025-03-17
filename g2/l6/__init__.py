"""
Пример 2. Двойные декораторы
"""
import time
from functools import lru_cache

def time_it(unit='s'):
    def decorator(func):
        def wrapper(*args, **kwargs):
            start = time.time()
            result = func(*args, **kwargs)
            end = time.time()

            elapsed = end - start

            if unit == 'ms':
                elapsed *= 1000
                print('Время работы функции', elapsed, 'миллисекунд')
            else:
                print('Время работы функции', elapsed, 'секунд')
            return result
        return wrapper
    return decorator

@time_it('s')
def sum_of_array(array):
    sum = 0
    for element in array:
        sum += element
    return sum

# start = time.time()
# print(sum_of_array([1, 2, 3, 4, 5, 1, 2, 3, 4, 5]))
# end = time.time()

# print('Время работы', end - start)



def cache(n):
    def decorator(func):
        func = lru_cache(maxsize=n)(func)
        return func
    return decorator

@time_it('s')
@cache(3)
def fibonacci(n):
    if (n < 2):
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

# print(fibonacci(50))
#
# print(fibonacci(50))


"""
Пример 3. Декораторы класса
"""
def permission_required(role):
    def decorator(cls):
        method = cls.execute
        def wrapper(self, *args, **kwargs):
            if self.role != role:
                raise PermissionError(f'{self.role} is not permitted')
            return method(self, *args, **kwargs)
        cls.execute = wrapper
        return cls
    return decorator

@permission_required('admin')
class AdminTask:
    def __init__(self, name, role):
        self.name = name
        self.role = role

    def execute(self):
        # if (self.role == 'admin'):
            print(f'{self.name} is working...')
        # else:
        #     raise PermissionError(f'{self.name} is not working')

u1 = AdminTask('u1', 'admin')
u2 = AdminTask('u2', 'user')

u1.execute()
u2.execute()


