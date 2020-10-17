# импортируем все зависимости
from parser import TextParser as TP
from remover import PersonalDataRemover as PDR


def main():
  filenames = ["1.txt", "2.txt", "5.txt", "6.txt"]

  for filename in filenames:
    tp = TP(filename=filename)

    data = tp.parse_file()

    print("Полученные текстовые данные:\n", data)

    pdr = PDR(data=data)

    result, removed = pdr.find_and_replace()

    print("Результат:\n", result)
    print("Удалённые вхождения:\n", removed)


if __name__ == "__main__":
  main()
