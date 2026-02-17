import statistics

temperatures = [20, 15, 32, 34, 21, 19, 25, 27, 30, 32, 34, 30, 29,
                25, 27, 22, 22, 23, 25, 29, 29, 31, 33, 31, 30, 32, 30, 28, 24, 23]

hot_days = list(filter(lambda t: t > 28, temperatures))
print(f'Список жарких дней: {hot_days}')

max_temp = max(hot_days)
print(f'Самая высокая температура: {max_temp}')

min_temp = min(hot_days)
print(f'Самая низкая температура: {min_temp}')

avg_temp = round(statistics.mean(hot_days), 2)
print(f'Средняя температура: {avg_temp}')
