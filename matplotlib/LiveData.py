from matplotlib import pyplot as plt 
import pandas as pd
from matplotlib.animation import FuncAnimation
import random
from itertools import count

plt.style.use('seaborn')

x = []
y = []

index = count()

def animate(i):
    # x.append(next(index))
    # y.append(random.randint(0, 10))

    # plt.cla()
    # plt.plot(x, y)
    data = pd.read_csv('data_gen.csv')
    x = data['x_value']
    y1 = data['total_1']
    y2 = data['total_2']

    plt.cla()
    plt.plot(x, y1, label='y1')
    plt.plot(x, y2, label='y2')

    plt.legend(loc='upper left')
    plt.tight_layout()


ani = FuncAnimation(plt.gcf(), animate, interval=1000)

plt.tight_layout()
plt.show()