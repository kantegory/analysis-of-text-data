#!/usr/bin/python3
# -*- coding: utf-8 -*-


# импортируем все зависимости
import io
import os
import re


class TextParser:
  """
  Класс для парсинга текстовых данных из .txt-файлов

  ...

  Атрибуты
  ----------
  path : str
    путь до директории с файлами
  encoding : str
    необходимая кодировка
  filename : str
    название файла, который необходимо спарсить

  Методы
  -------
  get_config():
    Возвращает текущие параметры парсера

  parse_file():
    Парсит файл, возвращает массив строк
  """

  def __init__(self, path=None, encoding=None, filename=None):
    """
    Конструктор для TextParser

    Параметры
    ----------
    :param path : str
      путь до директории с файлами
    :param encoding : str
      необходимая кодировка
    :param filename : str
      название файла, который необходимо спарсить
    """

    # присваиваем параметры, если они были указаны
    self.path = "./data" if not path else path
    self.encoding = "utf-8" if not encoding else encoding
    self.filename = "1.txt" if not filename else filename

  def get_config(self):
    """
    Формирует и возвращает объект config со всеми 
    параметрами парсера

    :return config: dict
    """

    config = {
      "path": self.path,
      "encoding": self.encoding,
      "filename": self.filename
    }

    return config

  def parse_file(self):
    """
    Парсит файл и возвращает массив строк

    :return data: list
    """

    # получаем полный путь до файла
    path = os.path.join(self.path, self.filename)

    # читаем файл
    file = io.open(path, mode="r", encoding=self.encoding)
    data = file.read()

    # закрываем его
    file.close()

    # получаем массив строк по переносам
    data = data.split("\n")
    s = " ".join(data)

    return s
