from pprint import pprint

def my_cook_book():
    with open('cook.txt', encoding='utf-8') as file:
        cook_book = {}
        for line in file.read().split('\n\n'):
            name, _, *args = line.split('\n')
            cook_li = []
            for arg in args:
                ingredient_name, quantity, measure = map(lambda x: int(x) if x.isdigit() else x, arg.split(' | '))
                cook_li.append({'ingredient_name': ingredient_name, 'quantity': quantity, 'measure': measure})
            cook_book[name] = cook_li
    return cook_book


def get_shop_list_by_dishes(dishes, person_count):
    new_cook = {}
    cook_book = my_cook_book()
    for dish in dishes:
        if dish in cook_book:
            for ingredient in cook_book[dish]:
                ingredient['quantity'] *= person_count
                new_cook.setdefault(ingredient['ingredient_name'], ingredient)

    dic_dish = {}
    for value in new_cook.values():
        name = value['ingredient_name']
        del value['ingredient_name']
        dic_dish[name] = value
    pprint(dic_dish)

get_shop_list_by_dishes(['Запеченный картофель', 'Омлет', 'Утка по-пекински'], 55)


import os
import os.path

def get_info_and_writing_to_list(file_names):
    '''Считывание содержимого файлов и запись информации в список'''
    my_data = []
    for file in file_names:
        with open(file, encoding='utf-8') as f:
            lines = f.read().splitlines()
            my_data.append([file, len(lines)])
            my_data[len(my_data)-1] += lines
    my_data.sort(key=len)
    return my_data


def writing_info_to_file(my_data, my_file):
    '''Запись в файл информации (создание файла при условии отсутствия другого с таким же именем)'''
    with open('corted.txt', 'w', encoding='utf-8') as f:
        for file in my_data:
            for elem in file:
                f.write(f'{elem}\n')
    file_path = os.path.join(os.getcwd(), my_file)
    return file_path

print(writing_info_to_file(get_info_and_writing_to_list(['1.txt', '2.txt', '3.txt']), 'corted.txt'))


