# Documentation - https://docs.scipy.org/doc/numpy/reference/routines.linalg.html

import numpy as np

a = [[9, 1, 1],
     [1, 8, 1],
     [1, 1, 7]]

n = 2
print("Возводит матрицу в степень n:\n", np.linalg.matrix_power(a, n))

print("#Некоторые характеристики матриц#")
print("Собственные значения и собственные векторы:\n", np.linalg.eig(a))

print("Определитель:\n", np.linalg.det(a))

print("Знак и логарифм определителя:\n", np.linalg.slogdet(a))

print("#Разложения#")
print("Разложение Холецкого:\n", np.linalg.cholesky(a))

print("QR разложение:\n", np.linalg.qr(a))

print("Сингулярное разложение:\n", np.linalg.svd(a))

print("#Системы уравнений#")

b = [1, 2, 3]
print("Решает систему линейных уравнений Ax = b:\n", np.linalg.solve(a, b))

print("Решает тензорную систему линейных уравнений Ax = b:\n",
      np.linalg.tensorsolve(a, b))

print("Метод наименьших квадратов:\n", np.linalg.lstsq(a, b))

print("Обратная матрица:\n", np.linalg.inv(a))
