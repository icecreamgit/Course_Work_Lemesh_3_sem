
class ValdSavidge:
    def __ValdFunction(self, matrix, m, n):
        minMassive = []
        T = 0

        for j in range(n):
            minTemporary = []
            for i in range(m):
                minTemporary.append(matrix[i][j])
            minMassive.append(min(minTemporary))
        T = max(minMassive)
        return T

    def MainValdSavidge(self, matrix):
        # matrix (m, n)
        m = len(matrix)
        n = len(matrix[0])
        TVald = self.__ValdFunction(matrix, m, n)
