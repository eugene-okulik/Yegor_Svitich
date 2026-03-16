import os
from datetime import datetime, timedelta

base_path = os.path.dirname(__file__)
print(base_path)
homework_path = os.path.dirname(os.path.dirname(base_path))
eugene_file_path = os.path.join(homework_path, 'eugene_okulik', 'hw_13', 'data.txt')
print(eugene_file_path)

with open(eugene_file_path, encoding='utf-8') as eugene_file:
    data = eugene_file.read()
    print(data)

def process_dates(lines):
    for line in lines:
        line = line.strip()
        try:
            number, rest = line.split('. ', 1) # отделяем номер задания до первой точки
            date_str, text = rest.split(' - ', 1) # по дефису отделяем дату от текста
            date = datetime.strptime(date_str.strip(), "%Y-%m-%d %H:%M:%S.%f")
            print(f'\nЗадание №{number}:')
            if number == '1':
                first_task = date + timedelta(weeks=1)
                print(f'Дата через неделю: {first_task}')
            elif number == '2':
                days_of_the_week = ['понедельник', 'вторник', 'среда', 'четверг', 'пятница', 'суббота', 'воскресенье']
                print(f'Это день недели: {days_of_the_week[date.weekday()]}')
            elif number == '3':
                now = datetime.now()
                third_task = now - date
                print(f'Эта дата была {third_task.days} дней назад')
        except Exception as error:
            print(f"Ошибка при обработке строки '{line}': {error}")

try:
    with open(eugene_file_path, 'r', encoding='utf-8') as data_file:
        results = data_file.readlines()
        process_dates(results)
except FileNotFoundError:
    print(f'Файл {eugene_file_path} не найден!')
