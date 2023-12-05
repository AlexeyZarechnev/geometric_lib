
def area(a, b):
    '''
    Возвращает площадь прямоугольника в десятичном формате

        Параметры:
        а (int) - первая сторона прямоугольника в десятичном формате
        b (int) - вторая сторона прямоугольника в десятичном формате

        Возвращаемое значение:
        area (int) - Площадь прямоугольника в десятичном формате

        Примеры вызова:
        print(area(2, 3))   \\ 6
        print(area(4, 1.5)) \\ 6
        print(area(5, 5))   \\ 25
    '''
    return a * b


def perimeter(a, b):
    '''
    Возвращает периметр прямоугольника в десятичном формате

        Параметры:
        а (int) - первая сторона прямоугольника в десятичном формате
        b (int) - вторая сторона прямоугольника в десятичном формате

        Возвращаемое значение:
        perimeter (int) - периметр прямоугольника в десятичном формате

        Пример вызова:
        print(perimeter(2, 3))   \\ 12
        print(perimeter(4, 1.5)) \\ 15
        print(perimeter(5, 5))   \\ 20
    '''
    return 2 * (a + b)