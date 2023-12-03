import numpy as np

class ValdSavidge:
    def __FindMaxElFromMatrix(self, matrix, m, n):
        maxMassive = []

        for j in range(n):
            maxTemporary = []
            for i in range(m):
                maxTemporary.append(matrix[i][j])
            maxMassive.append(max(maxTemporary))
        return maxMassive

    def __ValdFunction(self, matrix, m, n):
        minMassive = []
        T = 0.

        for j in range(n):
            minTemporary = []
            for i in range(m):
                minTemporary.append(matrix[i][j])
            minMassive.append(min(minTemporary))
        T = max(minMassive)
        return T
    def __SavidgeFunction(self, matrix, m, n):
        maxMassive = []
        regretList = np.zeros((m, n))
        T = 0.

        maxMassive = self.__FindMaxElFromMatrix(matrix, m, n)
        for j in range(n):
            for i in range(m):
                regretList[i][j] = abs(matrix[i][j] - maxMassive[j])
        maxMassive.clear()

        for j in range(n):
            maxTemporary = []
            for i in range(m):
                maxTemporary.append(regretList[i][j])
            maxMassive.append(max(maxTemporary))
        T = min(maxMassive)

        return T
    def MainValdSavidge(self, matrix):
        # matrix (m, n)
        m = len(matrix)
        n = len(matrix[0])
        TVald = self.__ValdFunction(matrix, m, n)
        TSavidge = self.__SavidgeFunction(matrix, m, n)
        return {"TVald": TVald, "TSavidge": TSavidge}
