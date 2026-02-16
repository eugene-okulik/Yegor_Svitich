import random

while True:
    salary = int(input("Введите вашу зарплату в долларах: "))
    if salary == -1:
        print('Завершение работы программы.')
        break
    bonus = random.choice([True, False])
    if bonus is True:
        bonus_amount = random.randrange(5, 5005, 5)
        total_salary = salary + bonus_amount
        print(f"{salary}, {bonus} - '${total_salary}'")
    else:
        print(f"{salary}, {bonus} - '${salary}'")
