import sys

print('Дефолтное ограничение на количество цифр:', sys.get_int_max_str_digits())
sys.set_int_max_str_digits(25000)
print('Теперь ограничение на количество цифр такое:', sys.get_int_max_str_digits())


def fibonacci_sequence():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


def get_fibonacci_element(n):
    fib_num = fibonacci_sequence()
    for x in range(n - 1):
        next(fib_num)
    return next(fib_num)


required_numbers = [5, 200, 1000, 100000]

for required_number in required_numbers:
    print(f'{required_number}-е число: {get_fibonacci_element(required_number)}')
