# TODO импортировать необходимые молули

import csv
import json

INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"


def task() -> None:

    with open(INPUT_FILENAME) as file:  #открываем csv файл для чтения # TODO считать содержимое csv файла
        lines = [line for line in csv.DictReader(file)] #читаем строки как словари

    with open(OUTPUT_FILENAME, "w") as file:  #открываем json файл для записи # TODO Сериализовать в файл с отступами равными 4
        json.dump(lines, file, indent=4) #записываем с отступами


if __name__ == '__main__':
    # Нужно для проверки
    task()

    with open(OUTPUT_FILENAME) as output_f:
        for line in output_f:
            print(line, end="")
