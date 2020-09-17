# Импорт билбиотеки
import numpy as np 

# Создание массива
a = np.array([1, 2, 3]) #одномерный
print(a)
print(type(a)) #тип

b = np.array([[1, 2, 3], [1.5, 2.5, 3.5]]) #двумерный
print(b)

b = np.array([[1, 2, 3], [4, 5, 6]], dtype=np.complex) #типизированный
print(b)

# Заполнение
z = np.zeros((3, 3)) #нулями
print(z)
o = np.ones((2, 2, 2)) #единицами
print(o)
e = np.eye(4) #единичная матрица
print(e)

print(np.empty((3, 3))) #пустой

print(np.arange(0, 21, 5)) #интервал с шагом
print(np.arange(1, 2, 0.1))

print(np.linspace(1, 9, 10)) #интервал с количеством

#sdjfjhsdjfs