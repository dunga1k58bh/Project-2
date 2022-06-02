
from ga.task import Task
import numpy as np
import pandas as pd
from random import random

class BinPacking(Task) :

    def __init__(self, file_path):
        super(BinPacking, self).__init__()

        data = pd.read_csv(file_path)
        self._capacity = int(data.columns[0])
        self._num_item = data.shape[0]
        self._dimention = self._num_item

        self._weight_item = data[data.columns[0]].to_numpy()


    #Decode individual in populations
    def decode(self, ind):
        x = []
        tmp_ind = ind.copy()

        if (len(tmp_ind) > self._dimention) :
            window = [random(),random()]
            stride = self.getStride(tmp_ind, window)

            # print(tmp_ind)
            i = 0
            while (i < len(tmp_ind)-1):
                tmp_x = 0
                for j in range (len(window)):
                    tmp_x = tmp_x + tmp_ind[i + j] * window[j]
                x.append(tmp_x)
                i+=stride
        else :
            x = tmp_ind

        sort_x = x.copy()
        sort_x.sort()
        solution = []
        for i in range(self._dimention):
            solution.append(x.index(sort_x[i]))

        return solution



    def evaluate(self, ind):
        num_bin = 0

        solution = self.decode(ind)
        tmp_capacity = 0
        for i in range(self._dimention):
            if (tmp_capacity + self._weight_item[solution[i]] > self._capacity):
                num_bin+=1
                tmp_capacity = self._weight_item[solution[i]]
            else:
                tmp_capacity += self._weight_item[solution[i]]
        num_bin += 1 #last bin
        return num_bin


    def checkInd(self, ind):

        solution = self.decode(ind)
        check = True
        for i in range(self._dimention):
            if i not in solution:
                check = False
                break
        return check