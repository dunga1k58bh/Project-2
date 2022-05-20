from dis import dis
from platform import node
from turtle import distance
from src.ga.task import Task
import numpy as np
import pandas as pd
import math

class TPS(Task) :

    def __init__(self, file_path):
        super(TPS, self).__init__()
        node_pd = pd.read_csv(file_path, sep = " ", usecols=[1,2])

        num_node = node_pd.shape[0]
        self.num_node = num_node

        node = node_pd.to_numpy()

        self.__distance = np.zeros((num_node, num_node))
        for i in range(num_node):
            for j in range(num_node):
                self.__distance[i, j] = math.sqrt(sum((node[i] - node[j])*(node[i] - node[j])))

        pass

    def evaluate(self, solution) -> float:
        distance = 0

        for i in range(solution.size()-1):
            distance += self.__distance[solution[i], solution[i+1]]

        distance += self.__distance[solution[0], solution[solution.size()-1]]

        return distance