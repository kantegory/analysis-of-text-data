#!/usr/bin/python3
# -*- coding: utf-8 -*-

# импортируем все зависимости
import re


class PersonalDataRemover:  
  """
  Класс для удаления персональных данных в соответствии с регулярным выражением

  ...

  Атрибуты
  ----------
  name_pattern : regexp
    паттерн для поиска ФИО
  replace_with : str
    символ, которым будет заменяться ФИО
  data : list
    массив строк, в которых нужно заменить ФИО

  Методы
  -------
  find_and_replace():
    Находит и заменяет все ФИО символ
    self.replace_with
  """

  def __init__(self, replace_with = None, data = None):
    """
    Конструктор для TextParser

    Параметры
    ----------
    :param replace_with : str
      символ, которым будет заменяться ФИО
    :param data : list
      массив строк, в которых нужно заменить ФИО
    """

    self.name_pattern = re.compile("((((ф|Ф).*?(и|И).*?(о|О).*?))|(в|В)рач.*|(п|П)ациент.*|((б|Б)ольного.*))")
    self.replace_with = "*" if not replace_with else replace_with
    self.data = data

  def find_and_replace(self):
    """
    Функция для поиска и замены всех ФИО на *.
    """
    removed_names = []
    result = []

    for i in range(len(self.data)):
      elem = self.data[i]

      if re.match(self.name_pattern, elem):
        elem_parts = elem.split(":")

        # пытаемся выделить части
        try:

          name = elem_parts[1]

          removed_names.append(elem_parts[1])

        # если у нас не получится, то будет брошен
        # exception IndexError, нам нужно продолжать
        except IndexError:
          continue
        
        # Проверяем наличие "." в имени
        if "." in name:
          name = name.split(".")
          name = "{} {}. {}.".format(self.replace_with, self.replace_with, self.replace_with)
        # если отсутствует, сплитим по пробелам
        else:
          name = name.split()
          name = "{} {} {}".format(self.replace_with, self.replace_with, self.replace_with)

        elem = "{} {}".format(elem_parts[0], name)

        result.append(elem)

      else:
        result.append(elem)

    return result, removed_names
