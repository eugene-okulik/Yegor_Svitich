results = [
    'результат операции: 42',
    'результат операции: 54',
    'результат работы программы: 209',
    'результат: 2'
]

def find_add_print(result):
    new_number = (int(result[result.index(':') + 1:])) + 10
    print(new_number)

for result in results:
    find_add_print(result)
