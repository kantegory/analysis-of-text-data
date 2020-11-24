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

  def __init__(self, replace_with=None, data=None):
    """
    Конструктор для TextParser

    Параметры
    ----------
    :param replace_with : str
      символ, которым будет заменяться ФИО
    :param data : list
      массив строк, в которых нужно заменить ФИО
    """

    self.name_pattern = re.compile("([А-Я]{1}[а-я]+)(\s)*([А-Я]{1}(\.|[а-я]+))(\s)*([А-Я]{1}(\.|[а-я]+))")
    self.email_pattern = re.compile("([a-z0-9_\.-]+)@([a-z0-9_\.-]+)\.([a-z\.]{2,6})")
    self.phone_pattern = re.compile("((8|\+7)[\- ]?)?(\(?\d{3}\)?[\- ]?)?[\d\- ]{7,10}")
    self.url_pattern = re.compile("(https?:\/\/(?:www\.|(?!www))[a-zA-Z0-9][a-zA-Z0-9-]+[a-zA-Z0-9]\.[^\s]{2,}|www\.[a-zA-Z0-9][a-zA-Z0-9-]+[a-zA-Z0-9]\.[^\s]{2,}|https?:\/\/(?:www\.|(?!www))[a-zA-Z0-9]+\.[^\s]{2,}|www\.[a-zA-Z0-9]+\.[^\s]{2,})")
    self.num_pattern = re.compile("№((\s)|(:))?((\s){0,8}(м/к)?(:)?(\s){0,4})[А-Яа-яA-Za-z0-9\/]{0,11}")
    self.date_pattern = [
      re.compile("\s*(3[01]|[12][0-9]|0?[1-9])(\.|\/|\s|\-|\:)((1[012]|0?[1-9])|((я|Я)нв(ар(ь|я))?|(ф|Ф)ев(рал(ь|я))?|(м|М)ар(т|та)?|(а|А)пр(ел(ь|я))?|(м|М)а(й|я)|(и|И)юн(ь|я)?|(и|И)юл(ь|я)?|(а|А)вг(ус(т|та))?|(с|С)ен(тябр(ь|я))?|(о|О)кт(ябр(ь|я))?|(н|Н)ояб(р(ь|я))?|(д|Д)ек(абр(ь|я))?))(\.|\/|\s|\-|\:)((?:19|20)\d{2})\s*"),
      re.compile("([0]?[1-9]|[1|2][0-9]|[3][0|1])[./-]([0]?[1-9]|[1][0-2])[./-]([0-9]{4}|[0-9]{2})"),
      re.compile("([0-1]?[0-9]|[2][0-3]\:)?([0-5][0-9])\:([0-5][0-9])")
      # re.compile("\s*(3[01]|[12][0-9]|0?[1-9])(\.|\/|\s|\-|\:)((я|Я)нв(ар(ь|я))?|(ф|Ф)ев(рал(ь|я))?|(м|М)ар(т|та)?|(а|А)пр(ел(ь|я))?|(м|М)а(й|я)|(и|И)юн(ь|я)?|(и|И)юл(ь|я)?|(а|А)вг(ус(т|та))?|(с|С)ен(тябр(ь|я))?|(о|О)кт(ябр(ь|я))?|(н|Н)ояб(р(ь|я))?|(д|Д)ек(абр(ь|я))?)")
    ]
    self.inn_pattern = re.compile("(?<=(ИНН))((\s)?\:(\s)?|(\s)?\-(\s)?|(\s))(\d{12})")
    self.snils_pattern = re.compile("(?<=(СНИЛС))((\s)?\:(\s)?|(\s)?\-(\s)?|(\s)|(\s|\:|\-){0,2}?\№(\s|\:|\-){0,2}?)(\d{3}\-\d{3}\-\d{3}\-\d{2})")
    self.passport_pattern = re.compile("(((П|п)аспорт(а)?))((\s)?\:(\s)?|(\s)?\-(\s)?|(\s)|(\s|\:|\-){0,2}?\№(\s|\:|\-){0,2}?)(\d{2}(\s)?\d{2}(\s)?\d{6})")
    self.replace_with = "*" if not replace_with else replace_with
    self.data = data

  def find_and_replace(self):
    """
    Функция для поиска и замены всех ФИО на *.
    """
    removed_names = []
    result = []

    # for i in range(len(self.data)):
    #   elem = self.data[i]
    #
    #   if re.match(self.name_pattern, elem):
    #     elem_parts = elem.split(":")
    #
    #     # пытаемся выделить части
    #     try:
    #
    #       name = elem_parts[1]
    #
    #       elem_parts[1] = elem_parts[1].strip()
    #
    #       removed_names.append(elem_parts[1])
    #
    #     # если у нас не получится, то будет брошен
    #     # exception IndexError, нам нужно продолжать
    #     except IndexError:
    #       continue
    #
    #     # Проверяем наличие "." в имени
    #     if "." in name:
    #       name = name.split(".")
    #       name = "{} {}. {}.".format(self.replace_with, self.replace_with, self.replace_with)
    #     # если отсутствует, сплитим по пробелам
    #     else:
    #       name = name.split()
    #       name = "{} {} {}".format(self.replace_with, self.replace_with, self.replace_with)
    #
    #     elem = "{} {}".format(elem_parts[0], name)
    elem = self.data
    if re.search(self.email_pattern, elem):
      while re.search(self.email_pattern, elem) is not None:
        match = re.search(self.email_pattern, elem)[0]
        elem = re.sub(self.email_pattern, "*", elem, 1)
        removed_names.append(match)

    if re.search(self.name_pattern, elem):
      while re.search(self.name_pattern, elem) is not None:
        match = re.search(self.name_pattern, elem)[0]
        elem = re.sub(self.name_pattern, "*", elem, 1)
        removed_names.append(match)

    # if re.search(self.phone_pattern, elem):
    #   while re.search(self.phone_pattern, elem) is not None:
    #     match = re.search(self.phone_pattern, elem)[0]
    #     elem = re.sub(self.phone_pattern, "*", elem, 1)
    #     removed_names.append(match)

    if re.search(self.url_pattern, elem):
      while re.search(self.url_pattern, elem) is not None:
        match = re.search(self.url_pattern, elem)[0]
        elem = re.sub(self.url_pattern, "*", elem, 1)
        removed_names.append(match)

    if re.search(self.num_pattern, elem):
      while re.search(self.num_pattern, elem) is not None:
        match = re.search(self.num_pattern, elem)[0]
        elem = re.sub(self.num_pattern, "*", elem, 1)
        removed_names.append(match)

    for regex in self.date_pattern:
      if re.search(regex, elem):
        while re.search(regex, elem) is not None:
          match = re.search(regex, elem)[0]
          elem = re.sub(regex, "*", elem, 1)
          removed_names.append(match)

    if re.search(self.inn_pattern, elem):
      while re.search(self.inn_pattern, elem) is not None:
        match = re.search(self.inn_pattern, elem)[0]
        elem = re.sub(self.inn_pattern, "*", elem, 1)
        removed_names.append(match)

    if re.search(self.passport_pattern, elem):
      while re.search(self.passport_pattern, elem) is not None:
        match = re.search(self.passport_pattern, elem)[0]
        elem = re.sub(self.passport_pattern, "*", elem, 1)
        removed_names.append(match)

    if re.search(self.snils_pattern, elem):
      while re.search(self.passport_pattern, elem) is not None:
        match = re.search(self.passport_pattern, elem)[0]
        elem = re.sub(self.passport_pattern, "*", elem, 1)
        removed_names.append(match)

    result.append(elem)

    return result, removed_names
