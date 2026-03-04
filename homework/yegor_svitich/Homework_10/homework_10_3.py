def smart_operation(func):

    def wrapper(first, second, operation):
        if first < 0 or second < 0:
            operation = '*'
        elif first == second:
            operation = '+'
        elif first > second:
            operation = '-'
        elif second > first:
            operation = '/'
        return func(first, second, operation)

    return wrapper


@smart_operation
def calc(first, second, operation=None):
    if operation == '+':
        return first + second
    elif operation == '-':
        return first - second
    elif operation == '*':
        return first * second
    elif operation == '/':
        return first / second


print("Программа запущена.")
print("Для выхода введите 'выход' или 'exit' вместо числа.\n")

while True:
    user_input1 = input("Введите первое число: ").lower().strip()
    if user_input1 in ['выход', 'exit']:
        break

    user_input2 = input("Введите второе число: ").lower().strip()
    if user_input2 in ['выход', 'exit']:
        break

    try:
        num1 = float(user_input1)
        num2 = float(user_input2)
        result = calc(num1, num2, None)
        print(f"Результат: {result}\n")

    except ValueError:
        print("Ошибка: введите корректное число или 'выход' для завершения.\n")

print("Программа завершена. До свидания!")
