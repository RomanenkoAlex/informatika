from math import *  # импортировал модуль математика


def task1():
    x = float(input('Введи x\n')) # Ввод данных
    y = float(input('Введи y\n'))
    z = float(input('Введи z\n'))

    a = (sin(x) - cos(y) ** 2) / (sin(x) ** 2 * cos(y) ** 2) # Расчет значений по формулам
    b = abs(z) ** (1 / 4) + cos(y) * sin(x) ** 2 + log(1 + y, 2)
    print('Значение а=', a) # Вывод данных
    print('Значение b=', b)


def task2():
    x = float(input('Введи x\n')) # Ввод данных
    a = 4 # константы
    b = -2
    f = sqrt(x) / (sqrt(x + a)) - x ** b # Расчет значения по формуле
    print('Значение f=', f)


def task3():
    x = float(input('Введи x\n')) # Ввод
    f = (sinh(cosh(x))) / (log(x + 1, 3)) # Расчет по формуле
    print('Значение f=', f) # Вывод


def task4():
    while True: # Цикл ожидания ввода корректных значений
        sphere_1_rad = float(input('Сфера №1\n')) # Радиус первой сферы
        sphere_2_rad = float(input('Сфера №2\n')) # Радиус второй сферы
        if sphere_1_rad > sphere_2_rad: # Проверка корректных значений
            V2 = 4 / 3 * pi * sphere_2_rad ** 3
            V1 = 4 / 3 * pi * sphere_1_rad ** 3
            V = V1 - V2
            otn = V / V2
            print('Отношение равно = ', "{:10.4f}".format(otn)) # Вывод
            break
        else:
            print('Сфера №1 должна быть больше Сфера №2, введите корректные значения')

def task5():
    temper_1 = float(input('Введите температуру №1: '))
    volume_1 = float(input('Введите объем №1: '))
    temper_2 = float(input('Введите температуру №2: '))
    volume_2 = float(input('Введите объем №2: '))
    vol_mix = volume_1 + volume_2 # Объем смеси
    temper_mix = (temper_1 * volume_1 + temper_2 * volume_2) / vol_mix # Температура смеси
    print('Объем смеси = ', "{:10.4f}".format(vol_mix))
    print('Температура смеси = ', "{:10.4f}".format(temper_mix))


def task6():
    while True: # Цикл ожидания ввода корректных значений
        volume_sphere = float(input('Введите объем сферы: '))
        if volume_sphere >=0: # Проверка корректного значения объема
            increase = int(input('Во сколько раз увеличить радиус: '))
            rad_sphere = ((3 / 4) * volume_sphere / pi) ** 1/3 # Нахождение радиуса через объем
            square_sphere_increase = 4 * pi * (rad_sphere * increase) ** 2 # Площадь поверхности увеличенной сферы
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
    D = A1 * B2 - B1 * A2 # Вычисление детерминанта
    if D == 0 : # Проверка совместности
        print('Система не имеет решений')
    else:
        x = (C1 * B2 - C2 * B1) / D
        y = (C2 * A1 - C1 * A2) / D
        print('x = ', "{:10.4f}".format(x))
        print('y = ', "{:10.4f}".format(y))


def task8():
    rad_sm = float(input('Введите радиус в см: '))
    rad_m = rad_sm / 100 # Перевод из сантиметров в метры
    rev_per_min = float(input('Введите обороты в минуту: '))
    frequency = rev_per_min / 60 # Частота
    w = 2 * pi * rev_per_min / 60 # Угловая скорость
    period = 1 / frequency # Вычисление периода
    centripetal_acceleration = w ** 2 * rad_m # центростремительное ускорение
    print('Частота вращения = ', "{:10.4f}".format(frequency))
    print('Период = ', "{:10.4f}".format(period))
    print('Угловая скорость = ', "{:10.4f}".format(w))
    print('Центростремительное ускорение = ', "{:10.4f}".format(centripetal_acceleration))

def task9():
    percent = 0.13 # процент налога
    salary = float(input('Введите зарплату до налога: '))
    salary_after_tax = salary * (1 - percent) # после налога
    print('Зарплата после налога = ', "{:10.4f}".format(salary_after_tax))
