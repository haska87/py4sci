# Импорт билбиотеки
import numpy as np

# cоздание одномерного массива
a = np.array([1, 2, 3])
print(a)
# вывод типа
print(type(a))

# cоздание двумерного массива
b = np.array([[1, 2, 3], [1.5, 2.5, 3.5]])
print(b)

# создание типизированного массива
b = np.array([[1, 2, 3], [4, 5, 6]], dtype=np.complex)
print(b)

# заполнение нулями
z = np.zeros((3, 3))
print(z)

# заполнение единицами
o = np.ones((2, 2, 2))
print(o)

# единичная матрица
e = np.eye(4)
print(e)

# пустой массив
print(np.empty((3, 3)))

# интервал с шагом
print(np.arange(0, 21, 5))
print(np.arange(1, 2, 0.1))

# интервал с количеством
print(np.linspace(1, 9, 10))
