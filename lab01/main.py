# импортируем все зависимости
from parser import TextParser as TP
from remover import PersonalDataRemover as PDR
from f1_score import F1_score as F1
import json
import os
import io

def main():

  ds = io.open("./data/dataset.json", mode="r")

  ds_json = ds.read()

  ds_json = json.loads(ds_json)

  ds.close()

  test_arr = []

  # filenames = [os.path.join(os.getcwd(), "data", "dataset2.txt")]

  # массив файлов, которые мы хотим обработать
  filenames = ["8.txt"] 

  # проходимся по массиву, парсим каждый из файлов
  for filename in filenames:
    tp = TP(filename=filename)

    # записываем всё в переменную
    data = tp.parse_file()

    # прогоняем алгоритм по замене персональных данных на *
    pdr = PDR(data=data)

    # выписываем полученный результат и удалённые вхождения
    result, removed = pdr.find_and_replace()

    print("Результат:\n", result)

    # записываем результат в файл
    result_file = open("result.txt", "w")
    result_file.write(result[0])
    result_file.close()

    print("Удалённые вхождения:\n", removed)

    # считаем F-меру
    f1 = F1(pred=removed, test=['test']).calculate()

    print("F-мера:\n", f1)

    print(len(removed))


if __name__ == "__main__":
  main()
