import pandas as pd
from matplotlib import pyplot as plt 
from collections import Counter
# import csv


# print(plt.style.available)
# plt.style.use('seaborn')

# with open('data.csv') as csv_file:
#     csv_reader = csv.DictReader(csv_file)

#     lang_counter = Counter()

#     for row in csv_reader:
#         lang_counter.update(row['LanguagesWorkedWith'].split(';'))

# print(lang_counter.most_common(20))

data = pd.read_csv('data.csv')
ids = data['Responder_id']
lang = data['LanguagesWorkedWith']

lang_counter = Counter()

for response in lang:
    lang_counter.update(response.split(';'))

languages = []
popularuty = []

for item in lang_counter.most_common(20):
    languages.append(item[0]) 
    popularuty.append(item[1])

languages.reverse()
popularuty.reverse()

plt.barh(languages, popularuty)
plt.title("Most popular programming languages")
plt.xlabel("Number")

plt.legend()
plt.tight_layout()
plt.show()