import random
import numpy as np

class CalculateY:
    def __ExponentialDestr(self, xMassive, n):
        nu = self.__MiddleX(xMassive, n)
        newList = sorted([(1. / nu * np.exp(-1. * xMassive[i] / nu)) for i in range(n)])
        return newList
    def __GenerateRandom(self, n):
        newList = [np.random.exponential() for i in range(n)]
        # newList = self.__ExponentialDestr(newList, n)
        return newList
    def __MiddleX(self, xMassive, n):
        sum = 0
        for i in range(n):
            sum += xMassive[i]
        return sum / n
    def ComputingY(self, n):
        x = self.__GenerateRandom(n)
        midValue = self.__MiddleX(x, n)
        Y = [x[i]/midValue for i in range(n)]
        return Y