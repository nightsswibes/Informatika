# TODO Напишите функцию для поиска индекса товара
def find_item_index(items_list, item):  # функция ищет индекс товара
    for index, current_item in enumerate(items_list):  # перебираем список с индексами
        if current_item == item:  # проверяем совпадение с искомым товаром
            return index  # возвращаем индекс первого найденного
    return None  # если не нашли, возвращаем None


items_list = ['яблоко', 'банан', 'апельсин', 'груша', 'киви', 'банан']  # список товаров

for find_item in ['банан', 'груша', 'персик']:  # перебираем товары для поиска
    index_item = find_item_index(items_list, find_item)  # вызываем функцию поиска
    if index_item is not None:  # проверяем найден ли товар
        print(f"Первое вхождение товара '{find_item}' имеет индекс {index_item}.")  # вывод результата
    else:
        print(f"Товар '{find_item}' не найден в списке.")  # вывод если не найден
