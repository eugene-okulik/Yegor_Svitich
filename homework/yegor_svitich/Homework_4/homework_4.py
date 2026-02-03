my_dict = {'tuple': (1, 2, 3, 4, 5, 6),
           'list': [1, 2, 3, 4, 5, 6],
           'dict': {'1': 'value1', '2': 'value2', '3': 'value3', '4': 'value4', '5': 'value5', '6': 'value6'},
           'set': {1, 2, 3, 4, 5, 6}
           }
print(my_dict)

print(my_dict['tuple'][-1])

my_dict['list'].append(7)
print(my_dict['list'])
my_dict['list'].pop(1)
print(my_dict['list'])

my_dict['dict'][('i am a tuple',)] = 'value7'
print(my_dict['dict'])
print(type(('i am a tuple',)))
my_dict['dict'].pop('1')
print(my_dict['dict'])

my_dict['set'].add(7)
print(my_dict['set'])
my_dict['set'].remove(1)
print(my_dict['set'])

print(my_dict)
