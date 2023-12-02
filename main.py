import BH.ThirdMethod
import HE.GetY
import HE.MethodOne
import KL.SecondMethod
import ValdSav.ValdSevMethod as vs

def write_In_File_Distr(Distr, N, name, n, Hi):
    with open("FILES\\"+ name + '_' + str(n) + '_' + str(N) + '_' + Hi + '.dat', 'w') as file:
        file.write(name + '(создано не ISW) N=' + str(N) + '\t n = ' + str(n) + ' ' + Hi + ' ' + '\n')
        file.write(str('0 ' + ' ' + str(N) + '\n'))
        for i in range(N):
            file.write(str(Distr[i]) + '\n')

def ReadFromFile():
    massive = []
    with open("ValdSav\\matrix.txt", 'r') as file:
        for line in file:
            elements = line.split()
            massive.append([float(i) for i in elements])
    return massive

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

def Crossroads(mode, params, YObject, HEObject, KLObject, BHObject):
    if mode == 0:
        HenzeFunction(params, YObject, HEObject)
        KlarFunction(params, YObject, KLObject)
        BHFunction(params, YObject, BHObject)


def Main():
    n = 100
    a = 1.
    N = 16600
    typeHypothesis = "H0"
    params = {"n": n, "a": a, "N": N, "typeHypothesis": typeHypothesis}

    YObject = HE.GetY.CalculateY()
    HEObject = HE.MethodOne.Henze()
    KLObject = KL.SecondMethod.Klar()
    BHObject = BH.ThirdMethod.BaringhauseHenze()
    ReadFromFile()
    # mode == 0 - рассчитываем статистики. 1 - метод Вальда и Сэвиджа, 2 - поиск необходимого объёма выборки
    # Crossroads(0, params, YObject, HEObject, KLObject, BHObject)

    el = vs.ValdSavidge()
    matrix = ReadFromFile()
    el.MainValdSavidge(matrix)


    flag = 0

Main()