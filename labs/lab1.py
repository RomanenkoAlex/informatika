from math import *  # импортировал модуль математика


def task1():
    x = float(input('Введи x\n'))
    y = float(input('Введи y\n'))
    z = float(input('Введи z\n'))

    a = (sin(x) - cos(y) ** 2) / (sin(x) ** 2 * cos(y) ** 2)
    b = abs(z) ** (1 / 4) + cos(y) * sin(x) ** 2 + log(1 + y, 2)
    print('Значение а=', a)
    print('Значение b=', b)


def task2():
    x = float(input('Введи x\n'))
    a = 4
    b = -2
    f = sqrt(x) / (sqrt(x + a)) - x ** b
    print('Значение f=', f)


def task3():
    x = float(input('Введи x\n'))
    f = (sinh(cosh(x))) / (log(x + 1, 3))
    print('Значение f=', f)


def task4():
    while True:
        sphere_1_rad = float(input('Сфера №1\n'))
        sphere_2_rad = float(input('Сфера №2\n'))
        if sphere_1_rad > sphere_2_rad:
            V2 = 4 / 3 * pi * sphere_2_rad ** 3
            V1 = 4 / 3 * pi * sphere_1_rad ** 3
            V = V1 - V2
            otn = V / V2
            print('Отношение равно = ', "{:10.4f}".format(otn))
            break
        else:
            print('Сфера №1 должна быть больше Сфера №2, введите корректные значения')

def task5():
    temper_1 = float(input('Введите температуру №1: '))
    volume_1 = float(input('Введите объем №1: '))
    temper_2 = float(input('Введите температуру №2: '))
    volume_2 = float(input('Введите объем №2: '))
    vol_mix = volume_1 + volume_2
    temper_mix = (temper_1 * volume_1 + temper_2 * volume_2) / vol_mix
    print('Объем смеси = ', "{:10.4f}".format(vol_mix))
    print('Температура смеси = ', "{:10.4f}".format(temper_mix))


def task6():
    while True:
        volume_sphere = float(input('Введите объем сферы: '))
        if volume_sphere >=0:
            increase = int(input('Во сколько раз увеличить радиус: '))
            rad_sphere = ((3 / 4) * volume_sphere / pi) ** 1/3
            square_sphere_increase = 4 * pi * (rad_sphere * increase) ** 2
            print('Площадь сферы = ', "{:10.4f}".format(square_sphere_increase))
            break
        else:
            print('Введите корректное значение объема')

def task7():
    A1 = float(input('Введите А1 :'))
    B1 = float(input('Введите В1 :'))
    C1 = float(input('Введите С1 :'))
    A2 = float(input('Введите А2 :'))
    B2 = float(input('Введите В2 :'))
    C2 = float(input('Введите С2 :'))
    D = A1 * B2 - B1 * A2
    if D == 0 :
        print('Система не имеет решений')
    else:
        x = (C1 * B2 - C2 * B1) / D
        y = (C2 * A1 - C1 * A2) / D
        print('x = ', "{:10.4f}".format(x))
        print('y = ', "{:10.4f}".format(y))


def task8():
    rad_sm = float(input('Введите радиус в см: '))
    rad_m = rad_sm / 100
    rev_per_min = float(input('Введите обороты в минуту: '))
    frequency = rev_per_min / 60
    w = 2 * pi * rev_per_min / 60
    period = 1 / frequency
    centripetal_acceleration = w ** 2 * rad_m
    print('Частота вращения = ', "{:10.4f}".format(frequency))
    print('Переод = ', "{:10.4f}".format(period))
    print('Угловая скорость = ', "{:10.4f}".format(w))
    print('Угловое ускорение = ', "{:10.4f}".format(centripetal_acceleration))

def task9():
    percent = 0.13
    salary = float(input('Введите зарплату до налога: '))
    salary_after_tax = salary * (1 - percent)
    print('Зарплата после налога = ', "{:10.4f}".format(salary_after_tax))

task7()