# TODO Напишите функцию find_common_participants
def find_common_participants(participants1, paricipants2, toget=','):

    participants_list1 = participants1.split(toget)
    participants_list2 = participants2.split(toget)

    common_participants = list(set(participants_list2.intersection.participants_list2))
    common_participants.sort()
    return common_participants
participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

participants = find_common_participants(participants_first_group, participants_second_group)
print("общие учасники" participants)
# TODO Провеьте работу функции с разделителем отличным от запятой
