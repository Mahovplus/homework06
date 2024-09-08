my_dict = {'Sunset' : 565656, 'Summer' : 101010}
print(my_dict)
print(my_dict.get('Sunset'))
print(my_dict.get('Oleg'))
my_dict.update({'Oleg' : 348893,
                'Richard' : 434395})
print(my_dict)
a = my_dict.pop('Sunset')
print(my_dict)
print(a)
print(my_dict)

my_set = {1, 1, 'error', 'error', True, True, ('power',  9999, 'power', 9999)}
print(my_set)
my_set.update({3, 4})
print(my_set)
my_set.remove('error')
print(my_set)