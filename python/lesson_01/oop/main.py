"""
Author: Mrgalaxxy
Title: OOP Python
Description: This code contains a simple example of an Object-Oriented Programming (OOP) concept in Python.
"""


#! класс
class Point:
  #! описание класса
  "Крутой класс ставлю респект"
  color='red'
  circle=3
#! екземпляры класса
a = Point()
#print(a)
#! вывод цвета класса
#print(a.color)
#! присвоение цвета класса к переменной
#color = a.color
#print(color)
#! удаление атрибута класса
#del Point.color
#! проверка наличия атрибута в экземпляре
#print(hasattr(Point, 'color'))
#! удаление атрибута экземпляра(2)
#delattr(Point, 'color')
#! просмотров атрибутов экземпляра
#print(a.__dict__)
#! вывод описания класса
print(Point.__doc__)