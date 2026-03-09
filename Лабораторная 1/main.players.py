list_players = ["Маша", "Петя", "Саша", "Оля", "Кирилл", "Коля"]

# индекс середины
middle_index = len(list_players) // 2

# разделяем на две команды, одна до середины списка, другая после середины списка
first_team = list_players[:middle_index]
second_team = list_players[middle_index:]

# выводим результат
print(first_team)
print(second_team)
