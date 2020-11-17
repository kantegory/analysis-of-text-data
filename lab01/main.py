# импортируем все зависимости
from parser import TextParser as TP
from remover import PersonalDataRemover as PDR
from f1_score import F1_score as F1
import json
import io

def main():

  ds = io.open("./data/dataset.json", mode="r")

  ds_json = ds.read()

  ds_json = json.loads(ds_json)

  ds.close()

  filenames = ["8.txt", "9.txt", "10.txt", "11.txt", "12.txt"]

  for filename in filenames:
    tp = TP(filename=filename)

    data = tp.parse_file()

    # print("Полученные текстовые данные:\n", data)

    pdr = PDR(data=data)

    result, removed = pdr.find_and_replace()


    print("Результат:\n", result)
    print("Удалённые вхождения:\n", removed)

    test_arr = ds_json[filename]

    print("Предполагаемые к удалению:\n", test_arr)

    f1 = F1(pred=removed, test=test_arr).calculate()

    print("F-мера:\n", f1)


if __name__ == "__main__":
  main()
