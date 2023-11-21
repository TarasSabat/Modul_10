my_dict = {'a': [1, 2, 3], 'b': [4, 5, 6], 'c': [7, 8, 9]}

# Замінити значення 2 на 5 для ключа 'a'
desired_key = 'a'
desired_value_to_replace = 2
new_value = 5

if desired_key in my_dict:
    # Отримати список значень для ключа 'a'
    values_list = my_dict[desired_key]

    # Замінити значення 2 на 5
    for i in range(len(values_list)):
        if values_list[i] == desired_value_to_replace:
            values_list[i] = new_value

print(my_dict)