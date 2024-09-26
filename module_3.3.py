def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)

print_params()                     # вызов функции без аргумента
print_params(345, 'Andrey') # вызов функйии с двумя аргументами
print_params(c = 5>1)

print_params(b = 25)
print_params(c = [1,2,3])


#Распаковка параметров: Создайте список values_list с тремя элементами разных типов.
#Создайте словарь values_dict с тремя ключами, соответствующими параметрам функции print_params, и значениями разных типов.
#Передайте values_list и values_dict в функцию print_params, используя распаковку параметров (* для списка и ** для словаря).

values_list = (262, 'Andrey', True)
values_dict = {'a': 1981, 'b': 'name', 'c': True}
print_params(*values_list)
print_params(**values_dict)

#Распаковка + отдельные параметры:
values_list_2 = (54.32, 'Строка')
print_params(*values_list_2, 42)