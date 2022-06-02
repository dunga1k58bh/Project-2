from random import random
from ga.task import Task
import numpy as np
import pandas as pd
import math


class TPS(Task) :

    def __init__(self, file_path):
        super(TPS, self).__init__()
        node_pd = pd.read_csv(file_path, sep = " ", usecols=[1,2])

        num_node = node_pd.shape[0]
        self.num_node = num_node

        self._dimention = num_node

        node = node_pd.to_numpy()

        self.__distance = np.zeros((num_node, num_node))
        for i in range(num_node):
            for j in range(num_node):
                self.__distance[i, j] = math.sqrt(sum((node[i] - node[j])*(node[i] - node[j])))

        pass


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
        distance = 0

        solution = self.decode(ind)

        for i in range(len(solution)-1):
            distance += self.__distance[solution[i], solution[i+1]]

        distance += self.__distance[solution[0], solution[len(solution)-1]]

        return distance


    def checkInd(self, ind):

        solution = self.decode(ind)
        check = True
        for i in range(self._dimention):
            if i not in solution:
                check = False
                break
        return check