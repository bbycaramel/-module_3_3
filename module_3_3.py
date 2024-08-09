def print_params(a=1, b='str', c=True):
    print(a, b, c)
print_params()
print_params(2)
print_params(3, 'text')
print_params(b=25)
print_params(c=[1, 2, 3])
values_list = [3.14, 'hello', False]
values_dict = {
    'a': 42,
    'b': 'world',
    'c': True
}
print("Распаковка из списка:")
print_params(*values_list)
print("Распаковка из словаря:")
print_params(**values_dict)

# Распаковка + отдельные параметры
values_list_2 = [54.32, 'Строка']
print("Распаковка + отдельные параметры:")
print_params(*values_list_2, 42)