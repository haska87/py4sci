import numpy as np

#Случаное заполнение
print(np.random.sample())
print(np.random.sample(5))
print(np.random.sample((3, 3)))

a = np.random.randint(-2, 2, 10) #[-2, 2), 10 штук
print("вектор из целых числел:", a)

b = np.random.randint(0, 4, (4, 4))
print("матрица из целых чисел:\n", b)

c = np.random.uniform(0, 10, (5, 5))
print("равномерное распределени:\n", c)

#Перемешивание
a = np.arange(10)
print("вектор:", a)
np.random.shuffle(a)
print("перемешанный1:", a)
print("перемешанный2:", np.random.permutation(a)) #перемешивает и возвращает
print("перемешанный3:", np.random.permutation(10)) #создает и перемешивает от 0 до 9

#Выбор
a = np.arange(10)
b = np.random.choice(a, 10, p=[0.5, 0.25, 0.25, 0, 0, 0, 0, 0, 0, 0])
print("вектор:", a)
print("выборка:", b)

#Генератор
print(np.random.random(10))
print(np.random.random(10))

#не случайная случайность
np.random.seed(100)
print(np.random.random(10))
np.random.seed(100)
print(np.random.random(10))