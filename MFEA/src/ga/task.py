from abc import ABC, abstractmethod


class Task:

    _dimention = 0
    _capacity = 0
    def __init__(self):
        pass

    @abstractmethod
    def makeSolution(self, solution):
        pass

    @abstractmethod
    def checkSolution(self, solution)->bool:
        pass

    @abstractmethod
    def evaluate(self, solution)->float:
        pass


    @abstractmethod
    def getlenGen():
        pass



