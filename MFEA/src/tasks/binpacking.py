from tkinter import E
from src.ga.task import Task
import numpy as np
import pandas as pd

class BinPacking(Task) :

    def __init__(self, file_path):
        super(BinPacking, self).__init__()

        data = pd.read_csv(file_path)
        self._capacity = int(data.columns[0])
        self._num_item = data.shape[0]

        self._weight_item = data[data.columns[0]].to_numpy()


    def evaluate(self, solution):
        c = 0

        for i in range(self._num_item):
            c += solution[i]*self._weight_item[i]

        return c

    def checkSolution(self, solution) -> bool:
        return self.evaluate(solution) <= self._capacity