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

  # test_data = ds_json["data"]["example1"]

  test_arr = []

  # for key, val in test_data.items():
  #   if key == "FIO":
  #     for _val in val:
  #       test_arr.append(_val)

  # print(test_arr)

  filenames = [os.path.join(os.getcwd(), "data" , "dataset2.txt")]

  # filenames = ["8.txt", "9.txt", "10.txt", "11.txt", "12.txt"]

  for filename in filenames:
    tp = TP(filename=filename)

    data = tp.parse_file()

    # print("Полученные текстовые данные:\n", data)

    pdr = PDR(data=data)

    result, removed = pdr.find_and_replace()


    print("Результат:\n", result)
    # with open("ans.txt", 'w') as file:
    #   for line in result:
    #     txt_file.write(" ".join(line) + "\n")  # works with any number of elements in a line

    print("Удалённые вхождения:\n", removed)

    # test_arr = ds_json[filename]

    print("Предполагаемые к удалению:\n", [])

    f1 = F1(pred=removed, test=['test']).calculate()

    print("F-мера:\n", f1)

    print(len(removed))


if __name__ == "__main__":
  main()
