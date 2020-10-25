import numpy as np


class F1_score():
    """
    F1_score считает F меру
    Inputs:
        pred: list(), shape (n_sample, n_predictions) массив слов, которые нашел парсер
        test: list(), shape (n_sample, n_test) массив истинных слов
    Outputs:
        F1, precision, recall - метрики
    """
    def __init__(self, pred, test):
        self.pred = pred
        self.test = test
        self.lenght = len(test)
        self.TP = 0
        self.FP = 0
        self.FN = 0

    def check(self, pred, test):
        # Проверка входных данных
        if len(np.array(self.pred, dtype=object).shape) == 1:
            self.pred = [self.pred]
        if len(np.array(self.test, dtype=object).shape) == 1:
            self.test = [self.test]

    def calculate(self):
        self.check(self.pred, self.test)

        for i in range(len(self.pred)):
            for elem in self.pred[i]:
                if elem in self.test[i]:
                    self.test[i].remove(elem)
                    self.TP += 1
                else:
                    self.FP += 1
            self.FN += len(self.test[i])
        
        accuracy = self.TP / self.lenght
        precision = self.TP / (self.TP + self.FP)
        recall = self.TP / (self.TP + self.FN)
        
        if precision == recall == 0:
            return 0
        else:
            f1 = (2 * precision * recall) / (precision + recall)
            return f1




# pred = [["123", "qqqq", "ghghgh", "kkk", "111"], ["ghghgh", "kkk", "111"]]
# test = [["00", "bb", "ghghgh", "kkk", "111"], ["3"]]
# score = F1_score(pred, test).calculate()
# print(score)





