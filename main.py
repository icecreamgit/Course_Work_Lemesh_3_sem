import HE.GetY
import HE.MethodOne
import KL.SecondMethod


def write_In_File_Distr(Distr, N, name, n):
    with open(name + '_' + str(n) + '_' + str(N) + '.dat', 'w') as file:
        file.write(name + '(создано не ISW) N=' + str(N) + '\t n = ' + str(n) +  ' ' + '\n')
        file.write(str('0 ' + ' ' + str(N) + '\n'))
        for i in range(N):
            file.write(str(Distr[i]) + '\n')


def HenzeFunction(params, YObject, HEObject):
    n = params["n"]
    a = params["a"]
    N = params["N"]
    saverHE = []

    for i in range(N):
        Y = YObject.ComputingY(n)
        HE = HEObject.MainHenze(Y, a, n)
        saverHE.append(HE)
        print(i)
    write_In_File_Distr(saverHE, N, "Henze", n)

def KlarFunction(params, YObject, KLObject):
    n = params["n"]
    a = params["a"]
    N = params["N"]
    saverKL = []

    for i in range(N):
        Y = YObject.ComputingY(n)
        KL = KLObject.MainKlar(Y, a, n)
        saverKL.append(KL)
        print(i)
    write_In_File_Distr(saverKL, N, "Klar", n)

def Main():
    n = 100
    a = 1.
    N = 16600
    params = {"n": n, "a": a, "N": N}

    YObject = HE.GetY.CalculateY()
    HEObject = HE.MethodOne.Henze()
    KLObject = KL.SecondMethod.Klar()

    # HEMassive = HenzeFunction(params, YObject, HEObject)
    KlarFunction(params, YObject, KLObject)



    l = 0



Main()