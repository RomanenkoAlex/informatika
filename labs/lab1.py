from math import * # импортировал модуль математика

def task1():
  x = float(input('Введи x\n'))
  y = float(input('Введи y\n'))
  z = float(input('Введи z\n'))
  
  a = (sin(x)-cos(y)**2)/(sin(x)**2*cos(y)**2)
  b = abs(z)**(1/4)+cos(y)* sin(x)**2+log(1+y, 2)
  print('Значение а=',a)
  print('Значение b=',b)

def task2():
  x = float(input('Введи x\n'))
  a = 4
  b = -2
  f = sqrt(x)/(sqrt(x+a))-x**b
  print('Значение f=', f)

def task3():
  x = float(input('Введи x\n'))
  f = (sinh(cosh(x)))/(log(x+1,3))
  print('Значение f=', f)

def task4():
  while True:
    sphere_1_rad = float(input('Сфера №1\n'))
    sphere_2_rad = float(input('Сфера №2\n'))
    if sphere_1_rad > sphere_2_rad:
      V2 = 4/3*pi*sphere_2_rad**3
      V1 = 4 / 3 * pi * sphere_1_rad ** 3
      V = V1-V2
      otn = V/V2
      print('Отношение равно = ',"{:10.4f}".format(otn))
      break
    else:
      print('Сфера №1 должна быть больше Сфера №2, введите корректные значения')

def task5():
  temper_1 = float(input('Введите температуру №1: '))
  volume_1 = float(input('Введите объем №1: '))
  temper_2 = float(input('Введите температуру №2: '))
  volume_2 = float(input('Введите объем №2: '))
  vol_mix = volume_1 + volume_2
  temper_mix = (temper_1 * volume_1 + temper_2 * volume_2)/vol_mix
  print('Объем смеси = ', "{:10.4f}".format(vol_mix))
  print('Температура смеси = ', "{:10.4f}".format(temper_mix))

