
def print_params(a=1, b='строка', c=True):
    print(a, b, c)


values_list = [6, 'цифра', False]
values_dict = {'a': 8, 'b': 24, 'c': 75}
values_list_2 = [54.32, 'Строка']
print_params(*values_list_2, 42)
print_params(*values_list,)
print_params(**values_dict)
print_params(b = 30)
