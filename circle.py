import math


def area(r):
    """
    Возвращает площадь круга с радиусом r
    
    Параметры:
    r (int, float): Радиус круга
    
    Возвращаемое значение:
    int, float: Площадь круга (math.pi*r*r)

    Пример вызова:
    >>> area(3)
    28.274333882308138
    
    """
    if r < 0:
        raise ValueError("Отрицательный радиус")
    return math.pi * r * r


def perimeter(r):
    """
    Возвращает длину окружности радиуса r

    Параметры:
    r (int, float): Радиус круга

    Возвращаемое значение:
    int, float: длина окружности (2*math.pi*r)

    Пример вызова:
    >>> perimeter(3)
    18.84955592153876
    """
    if r < 0:
        raise ValueError("Радиус не может быть отрицательным")
    return 2 * math.pi * r
