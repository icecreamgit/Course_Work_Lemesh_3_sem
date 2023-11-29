import GetY
import MethodOne



def Main():
    n = 10
    a = 1
    YObject = GetY.CalculateY()
    HEObject = MethodOne.Henze()


    Y = YObject.ComputingY(n)
    HE = HEObject.MainHenze(Y, a, n)


    l = 0



Main()