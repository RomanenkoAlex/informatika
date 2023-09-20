from math import * # импортировал модуль математика

def task1():
  x = float(input('Введи x'))
  y = float(input('Введи y'))
  z = float(input('Введи z'))
  
  a = (sin(x)-cos(y)**2)/(sin(x)**2*cos(y)**2)
  b = abs(z)**(1/4)+cos(y)* sin(x)**2+log(1+y, 2)
  print('Значение а=',a)
  print('Значение b=',b)

def task2():
  x = float(input('Введи x'))
  
  

task1()