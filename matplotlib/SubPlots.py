from matplotlib import pyplot as plt
import pandas as pd

plt.style.use('seaborn')

data = pd.read_csv('data_subplots.csv')
ages = data['Age']
dev_all = data['All_Devs']
dev_py = data['Python']
dev_js = data['JavaScript']

# plt.plot(ages, dev_all, label="All Devs")
# plt.plot(ages, dev_py, label="Python")
# plt.plot(ages, dev_js, label="JS")

# fig1, (ax1, ax2) = plt.subplots(2, 1, sharex=True)
fig1, ax1 = plt.subplots()
fig2, ax2 = plt.subplots()

ax1.plot(ages, dev_all, label='All Devs', linestyle='--', color='black')
ax1.set_title("Средняя зарплата программиста")
ax1.set_ylabel("Зарплата в USD")

ax2.plot(ages, dev_py, label="Python")
ax2.plot(ages, dev_js, label="JS")
ax2.set_xlabel("Возраст")
ax2.set_ylabel("Зарплата в USD")

fig1.savefig('all_dev.png')
fig2.savefig('others_dev.png')

plt.legend()
plt.tight_layout()
plt.show()
