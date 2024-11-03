"""
Создать класс прямоугольник:
а) при создании указывается ширина и длина
б) методы для площади и периметра
    # возвращает площадь
    # периметр
в) масштабирование и поворот
    r1.scale(10) - высота и ширина увеличиваются в 10 раз
    r1.scale(0.1) - высота и ширина уменьшаются в 10 раз
    r1.rotate() - меняется ширина и высота местами
"""


class Rect:
    def __init__(self, a=0, b=0):
        self.a = a
        self.b = b

    def area(self):
        return self.a*self.b

    def perimeter(self):
        return self.a*2 + self.b*2

    def scale(self, value):
        print(self.a*value, round(self.b*value, 2))

    def rotate(self):
        self.a, self.b = self.b, self.a
        print(self.a, self.b)


def task_1_3():
    r1 = Rect(10, 56)

    print(r1.area())  # возвращает площадь
    print(r1.perimeter())  # периметр

    r1.scale(10)  # высота и ширина увеличиваются в 10 раз
    r1.scale(0.1)  # высота и ширина уменьшаются в 10 раз
    r1.rotate()  # меняется ширина и высота местами