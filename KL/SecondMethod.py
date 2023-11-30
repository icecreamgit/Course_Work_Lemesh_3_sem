import numpy as np

class Klar:

    def __C0(self, a, n):
        result = 2.*(3.*a + 2.)*n / ((2.+a) * pow((1.+a), 2))
        return result

    def __C1(self, Y, a, n):
        sum = 0.
        for j in range(n):
            sum += np.exp(-(1.+a)*Y[j]) / pow((1.+a), 2)
        return 2. * pow(a, 3) * sum

    def __C2(self, Y, a, n):
        sum = 0.
        for j in range(n):
            sum += np.exp(-a * Y[j])
        return 2. * sum / n

    def __C3(self, Y, a, n):
        sum = 0.
        for k in range(n):
            for j in range(n):
                if (j < k):
                    sum += ((a*(Y[k]-Y[j]) - 2.) * np.exp(-a * Y[j]))
                else:
                    break

        return 2. * sum / n

    def MainKlar(self, Y, a, n):
        KL = self.__C0(a, n) - self.__C1(Y, a, n) - self.__C2(Y, a, n) + self.__C3(Y, a, n)
        return KL