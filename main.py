import GetY
import MethodOne

def write_In_File_Distr(Distr, N, name, n):
    with open(name + '_' + str(n) + '_' + str(N) + '.dat', 'w') as file:
        file.write(name + '(создано не ISW) N=' + str(N) + '\t n = ' + str(n) +  ' ' + '\n')
        file.write(str('0 ' + ' ' + str(N) + '\n'))
        for i in range(N):
            file.write(str(Distr[i]) + '\n')


def Main():
    n = 100
    a = 1.
    saverHE = []
    N = 16600

    YObject = GetY.CalculateY()
    HEObject = MethodOne.Henze()

    for i in range(N):
        Y = YObject.ComputingY(n)
        HE = HEObject.MainHenze(Y, a, n)
        saverHE.append(HE)
        print(i)
    write_In_File_Distr(saverHE, N, "Henze", n)


    l = 0



Main()