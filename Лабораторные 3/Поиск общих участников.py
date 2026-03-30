# TODO Напишите функцию find_common_participants
def find_common_participants(group1, group2, separator=","):  #функция поиска общих участников
    list1 = group1.split(separator)  #разбиваем строку в список
    list2 = group2.split(separator)  #разбиваем вторую строку

    common = list(set(list1).intersection(set(list2)))  #находим пересечение списков
    common.sort()  #сортируем список по алфавиту

    return common  #возвращаем список общих участников


participants_first_group = "Иванов|Петров|Сидоров"  #первая группа участников
participants_second_group = "Петров|Сидоров|Смирнов"  #вторая группа участников


# TODO Провеьте работу функции с разделителем отличным от запятой
result = find_common_participants(participants_first_group, participants_second_group, "|")
print(result)