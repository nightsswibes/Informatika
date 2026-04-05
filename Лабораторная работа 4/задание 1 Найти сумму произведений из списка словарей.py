# TODO решите задачу

import json

def task() -> float:
    file = "input.json"

    with open(file) as f: #открываем файл для чтения
        data = json.load(f) #читаем данные внутри этого файла

    summa = 0

    for i in data: #перебор всех элементов
        proizvedenie = i["score"] * i["weight"] #считаем произведение значений
        summa += proizvedenie #сумма произведений значений

    return round(summa, 3) #значение, округленное до 3 знаков после запятой

print(task())