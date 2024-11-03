# Написать класс PointXY, у которого есть атрибуты x и y.
import math


class PointXY:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    # методы
    def distance_from_zero(self):
        #  расстояние от начала координат до этой точки
        distance = math.sqrt(abs(self.x)**2 + abs(self.y)**2)
        return distance

    def distance_to(self, point):
        #  расстояние от точки до другой точки
        distance = math.sqrt(abs(self.x - point.x) ** 2 + abs(self.y - point.y) ** 2)
        return distance


def task_1_1():
    # 1.1(a)
    # Без конструктора
    p0 = PointXY()
    p4 = PointXY()
    p0.x = 1
    p0.y = 5
    p4.x = 8
    p4.y = 7
    # С конструктором:
    p1 = PointXY(1, 3)
    p2 = PointXY(4, 5)

    d0 = p0.distance_from_zero()
    d4 = p4.distance_from_zero()
    d1 = p1.distance_from_zero()
    d2 = p2.distance_from_zero()
    print(d0, d1, d2, d4)

    # 1.1(б)
    d = p0.distance_to(p4)
    print(d)
