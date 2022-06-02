from abc import ABC, abstractmethod


class Task:

    _dimention = 0


    def getStride(self, temp_ind, window):
        stride = 0

        len_ind = len(temp_ind)
        if (len_ind - len(window)) % (self._dimention -1) == 0:
            return (len_ind - len(window)) / (self._dimention -1)

        stride = int((len_ind - len(window)) / (self._dimention)) + 1;

        padding = stride*(self._dimention-1) + len(window) - len_ind
        for i in range(padding):
            temp_ind.append(0.0)
        return stride




    @abstractmethod
    def makeInd(self, ind):
        pass

    @abstractmethod
    def checkInd(self, ind):
        pass

    @abstractmethod
    def evaluate(self, ind):
        pass


    @abstractmethod
    def getlenGen():
        pass

    @abstractmethod
    def decode():
        pass



