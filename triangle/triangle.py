
def area(a, h):
    '''
    Возвращает площадь треугольника в десятичном формате

        Параметры:
        а (int) - основание треугольника в десятичном формате
        h (int) - высота треугольника в десятичном формате

        Возвращаемое значение:
        area (int) - Площадь треугольника в десятичном формате

        Примеры вызова:
        print(area(2, 1))    \\ 1
        print(area(4, 3))    \\ 6
        print(area(5, 10))   \\ 25
    '''
    return a * h / 2        # TODO исправить ошибки

def perimeter(a, b, c):
    '''
    Возвращает периметр треугольника в десятичном формате

        Параметры:
        а (int) - 1 сторона треугольника в десятичном формате
        b (int) - 2 сторона треугольника в десятичном формате
        c (int) - 3 сторона треугольника в десятичном формате

        Возвращаемое значение:
        perimeter (int) - периметр треугольника в десятичном формате

        Примеры вызова:
        print(perimeter(2, 5, 4))   \\ 11
        print(perimeter(4, 4, 1))   \\ 9
        print(perimeter(5, 5, 3))   \\ 13
    '''
    return a + b + c        # TODO исправить ошибки
