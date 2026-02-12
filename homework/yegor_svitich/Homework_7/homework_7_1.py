hidden_number = 3

while True:
    user_input = int(input('Угадайте число (от 0 до 5): '))
    if user_input == hidden_number:
        print('Поздравляю! Вы угадали!')
        break
    elif user_input < 0 or user_input > 5:
        print(f'Число {user_input} не находится в промежутке от 0 до 5, введите число из этого промежутка')
    else:
        print('Попробуйте снова')
