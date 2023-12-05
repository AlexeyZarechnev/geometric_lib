import math

def area(r):
    '''
    Возвращает площадь круга в десятичном формате

        Параметры:
        r (int) - радиус круга в десятичном формате

        Возвращаемое значение:
        area (int) - площадь круга в десятичном формате

        Примеры вызова:
        print(area(2))  \\ 12,566370614359173
        print(area(4))  \\ 50,265482457436692
        print(area(5))  \\ 78,539816339744831
    '''
    return math.pi * r * r


def perimeter(r):
    '''
    Возвращает периметр круга в десятичном формате

        Параметры:
        r (int) - радиус круга в десятичном формате

        Возвращаемое значение:
        perimetr (int) - периметр круга в десятичном формате

        Примеры вызова:
        print(perimeter(2))  \\ 12,566370614359173
        print(perimeter(4))  \\ 25,132741228718346
        print(perimeter(5))  \\ 31,415926535897932
    '''
    return 2 * math.pi * r