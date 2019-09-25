# Импорт билбиотеки
import numpy as np 

# Создание массива
a = np.array([1, 2, 3]) #одномерный
print(a)
print(type(a))

b = np.array([[1.5, 2, 3], [4, 5, 6]]) #двумерный
print(b)

b = np.array([[1.5, 2, 3], [4, 5, 6]], dtype=np.complex) #типизированный
print(b)

# Заполнение
z = np.zeros((3, 5)) #нулями
print(z)
o = np.ones((2, 2, 2)) #единицами
print(o)
e = np.eye(5) #единичная матрица
print(e)

print(np.empty((3, 3))) #пустой

print(np.arange(10, 30, 5)) #интервал с шагом
print(np.arange(0, 1, 0.1))

print(np.linspace(0, 9, 10)) #интервал с количеством