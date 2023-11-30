class BaringhauseHenze:

    def __C0(self, Yj, Yk, a):
        result = (1.-Yj) * (1.-Yk) / (Yj+Yk+a)
        return result

    def __C1(self, Yj, Yk, a):
        result = (2.*Yj*Yk-Yj-Yk) / pow((Yj+Yk+a), 2)
        return result

    def __C2(self, Yj, Yk, a):
        result = (2*Yj*Yk) / pow((Yj+Yk+a), 3)
        return result

    def MainBaringhauseHenze(self,Y, a, n):
        sum = 0.
        for k in range(n):
            for j in range(n):
                sum += (self.__C0(Y[j], Y[k], a) + self.__C1(Y[j], Y[k], a) + self.__C2(Y[j], Y[k], a))
        sum /= n
        return sum