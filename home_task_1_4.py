"""
1.4 Прямоугольник по двум точкам
На основе предыдущих двух задач (PointXY и Rect) сделать прямоугольник, у которого задаются координаты вершин.
Стороны при этом всегда параллельны осям координат, то есть для задания достаточно двух точек (вершин).
а) при создании указываются две любые вершины типа PointXY
б) то же самое, но внутри хранить именно нижний левый и верхний правый углы
в) сделать метод, которым можно проверить, лежит ли точка внутри прямоугольника
г) аналогично пункту в) сделать зеркальный метод у класса PointXY: теперь спрашиваем у точки, лежит ли она внутри указанного прямоугольника
"""


class PointXY:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def is_inside(self, rect):
        if self.x in range(rect.p1_x, rect.p2_x) and self.y in range(rect.p1_y, rect.p2_y):
            return "точка находится внутри прямоугольника"
        else:
            return "точка не находится внутри прямоугольника"


class RectA:
    def __init__(self, p1, p2):
        self.p1_x = p1.x
        self.p1_y = p1.y
        self.p2_x = p2.x
        self.p2_y = p2.y

    def area(self):
        side_a = abs(self.p1_x - self.p2_x)
        side_b = abs(self.p1_y - self.p2_y)
        return side_a * side_b

    def has_inside(self, point):
        if point.x in range(self.p1_x, self.p2_x) and point.y in range(self.p1_y, self.p2_y):
            return "точка находится внутри прямоугольника"
        else:
            return "точка не находится внутри прямоугольника"


class RectB:
    # б) то же самое, но внутри хранить именно нижний левый и верхний правый углы
    def __init__(self, p1, p2):
        self.p1_x = min(p1.x, p2.x)
        self.p1_y = min(p1.y, p2.y)
        self.p2_x = max(p1.x, p2.x)
        self.p2_y = max(p1.y, p2.y)


def task_1_4():
    p1 = PointXY(1, 2)
    p2 = PointXY(5, 6)

    r2 = RectA(p1, p2)
    print(r2.area())

    r3 = RectB(p1, p2)
    print("lower left x: %s \nlower left y: %s \nupper right x: %s \nupper right y: %s"
          % (r3.p1_x, r3.p1_y, r3.p2_x, r3.p2_y))

    # point into Rang
    p3 = PointXY(3, 3)
    print(r2.has_inside(p3))
    # point outside Rang
    p4 = PointXY(6, 9)
    print(r2.has_inside(p4))

    # находится ли point1 внутри rang1
    p3 = PointXY(3, 3)
    print(p3.is_inside(r2))
    p4 = PointXY(6, 9)
    print(p4.is_inside(r2))
