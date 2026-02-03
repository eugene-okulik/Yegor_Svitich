string_1 = 'результат операции: 42'
string_2 = 'результат операции: 514'
string_3 = 'результат работы программы: 9'

colon_index = string_1.index(':')
result = (int(string_1[colon_index + 1:])) + 10
print(result)

colon_index = string_2.index(':')
result = (int(string_2[colon_index + 1:])) + 10
print(result)

colon_index = string_3.index(':')
result = (int(string_3[colon_index + 1:])) + 10
print(result)
