import numpy as np

# Базовые операции
a = np.arange(10, 60, 10)
b = np.arange(5)

print(a + b)
print(a - b)

print(a * b)
print(a / b)

# деление по модулю (остаток)
print(a % b)
# целочисленное деление
print(a // b)
# возведение в степень
print(a ** b)

# операции с числами
print(a + 1)
print(a * 2)
print(a < 40)

# математические операции
print(np.sqrt(a))
print(np.cos(a))
print(np.log(a))

# сумма и максимум
print(np.sum(a))
print(np.max(a))

# индексы и срезы
a = np.arange(10) ** 2
print(a)
print(a[1])
print(a[2:5])

a[2:5] = -1
print(a)
# обратный вывод
print(a[::-1])

a = np.array([[0, 1, 2, 3],
              [10, 11, 12, 13],
              [20, 21, 22, 23],
              [30, 31, 32, 33],
              [40, 41, 42, 43]])

print(a[2, 2])
print(a[(2, 2)])
print(a[2][2])

# первая строка
print(a[:, 0])
# последняя строка
print(a[-1])
# с 3 строки
print(a[3:])

for row in a:
    print(row)

for el in a.flat:
    print(el)

# манипуляции с формой
print(a)
# вывод формы
print(a.shape)
# сделать плоским
print(a.ravel())
# транспонирование
print(a.transpose())

# изменить форму
a.shape = (4, 5)
print(a)

# возращает измененную форму
print(a.reshape(5, 4))
print(a)

# изменяет форму
a.resize((5, 4))
print(a)

# объединение и разбиение
a = np.array([[1, 2], [3, 4]])
b = np.array([[5, 6], [7, 8]])
print(np.vstack((a, b)))
print(np.hstack((a, b)))

print(np.column_stack((a, b)))
print(np.row_stack((a, b)))

a = np.arange(12).reshape((2, 6))
print(a)
print(np.hsplit(a, 3))

# копии
a = np.arange(10)
b = a
print(b is a)

b.shape = (2, 5)
print(a.shape)

# поверхностная копия (представление)
c = a.view()
print(c)
print(c is a)
print(c.base is a)

# форма а не поменяется
c.shape = (5, 2)
print(a.shape)
# данные а изменятся
c[0, 0] = 99
# cрез массива это представление
print(a)

# глубокая копия
d = a.copy()
print(d is a)
print(d.base is a)

d[0, 0] = 9999
print(a)
