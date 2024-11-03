"""
1.2 Автомобиль
Сделать класс Car
а) У машины должны быть атрибуты:
    "сколько бензина в баке"
    "вместимость бака" - сколько максимум влезаем бензина
    "расход топлива на км"
б) метод "залить столько-то литров в бак"
    должна учитываться вместительность бака если пытаемся залить больше, чем вмещается, то заполняется полностью
    print'ом выводится сообщение о лишних литрах
в) метод "проехать сколько-то км"
    выведет принт "проехали ... километров" в результате поездки потратится бензин
    если бензина не хватает, машина всё равно едет, пока не кончится бензин
г) добавить атрибут с пробегом, который увеличивается в результате ride
★
д) сделать так, чтобы расход топлива увеличивался на 5% каждые 1000км.
    Здесь можно либо увеличивать пробег скачкообразно каждые 1000км, можно увеличивать более плавно каждый км, а можно вспомнить школьные интегралы.
"""


class Car:
    def __init__(self, gas_l=30, capacity_l=40, l_per_km=0.1, mileage=0):
        self.gas_l = gas_l
        self.capacity_l = capacity_l
        self.l_per_km = l_per_km
        self.mileage = mileage

    def fill(self, amount):
        self.gas_l = self.gas_l + amount
        if self.gas_l > self.capacity_l:
            print("Extra liters: %s" % (self.gas_l - self.capacity_l))
            self.gas_l = self.capacity_l
        return self.gas_l

    def ride(self, distance):
        mileage_check = int(self.mileage / 1000)
        while mileage_check > 0:
            self.l_per_km += self.l_per_km*0.05
            mileage_check -= 1

        gas_spend = self.l_per_km * distance
        if gas_spend < self.capacity_l:
            print("проехали %s километров, в результате поездки потратится бензин %s" % (distance, gas_spend))
            self.mileage += distance
            return self.gas_l - gas_spend
        else:
            distance = self.capacity_l / self.l_per_km
            self.mileage += distance
            self.gas_l = 0
            print("проехали %s километров, в результате поездки потратится весь бензин" % distance)


def task_1_2():
    c1 = Car()
    # first fill and ride
    print("Gas in tank: %s" % c1.fill(5))
    print("Gas in tank after ride: %s" % c1.ride(50))
    print("Car 1 status:\n gas_l = %s \n capacity_l = %s \n l_per_km = %s \n mileage = %s"
          % (c1.gas_l, c1.capacity_l, c1.l_per_km, c1.mileage))
    # second fill and ride with big values
    print("Gas in tank: %s" % c1.fill(50))
    print("Gas in tank after ride: %s" % c1.ride(500))
    print("Car 1 status:\n gas_l = %s \n capacity_l = %s \n l_per_km = %s \n mileage = %s"
          % (c1.gas_l, c1.capacity_l, c1.l_per_km, c1.mileage))
