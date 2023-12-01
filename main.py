import BH.ThirdMethod
import HE.GetY
import HE.MethodOne
import KL.SecondMethod


def write_In_File_Distr(Distr, N, name, n, Hi):
    with open("FILES\\"+ name + '_' + str(n) + '_' + str(N) + '_' + Hi + '.dat', 'w') as file:
        file.write(name + '(создано не ISW) N=' + str(N) + '\t n = ' + str(n) +  ' ' + '\n')
        file.write(str('0 ' + ' ' + str(N) + '\n'))
        for i in range(N):
            file.write(str(Distr[i]) + '\n')


def HenzeFunction(params, YObject, HEObject):
    n = params["n"]
    a = params["a"]
    N = params["N"]
    typeHypothesis = params["typeHypothesis"]
    saverHE = []

    for i in range(N):
        Y = YObject.ComputingY(n, typeHypothesis)
        HE = HEObject.MainHenze(Y, a, n)
        saverHE.append(HE)
        print(i)
    write_In_File_Distr(saverHE, N, "Henze", n, typeHypothesis)
    saverHE.clear()

def KlarFunction(params, YObject, KLObject):
    n = params["n"]
    a = params["a"]
    N = params["N"]
    typeHypothesis = params["typeHypothesis"]
    saverKL = []

    for i in range(N):
        Y = YObject.ComputingY(n, typeHypothesis)
        KL = KLObject.MainKlar(Y, a, n)
        saverKL.append(KL)
        print(i)
    write_In_File_Distr(saverKL, N, "Klar", n, typeHypothesis)
    saverKL.clear()

def BHFunction(params, YObject, BHObject):
    n = params["n"]
    a = params["a"]
    N = params["N"]
    typeHypothesis = params["typeHypothesis"]
    saverBH = []

    for i in range(N):
        Y = YObject.ComputingY(n, typeHypothesis)
        BH = BHObject.MainBaringhauseHenze(Y, a, n)
        saverBH.append(BH)
        print(i)
    write_In_File_Distr(saverBH, N, "Baringhause_Henze", n, typeHypothesis)
    saverBH.clear()


def Main():
    n = 10
    a = 1.
    N = 16600
    typeHypothesis = "H2"
    params = {"n": n, "a": a, "N": N, "typeHypothesis": typeHypothesis}

    YObject = HE.GetY.CalculateY()
    HEObject = HE.MethodOne.Henze()
    KLObject = KL.SecondMethod.Klar()
    BHObject = BH.ThirdMethod.BaringhauseHenze()

    # HEMassive = HenzeFunction(params, YObject, HEObject)
    # KlarFunction(params, YObject, KLObject)
    # BHFunction(params, YObject, BHObject)


    l = 0



Main()