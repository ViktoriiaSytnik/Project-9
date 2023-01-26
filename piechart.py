import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('titles.csv')

movie = df['title']
ages = df['age_certification']
map = {}


nanAge = ages[4]

for age in ages:
    if age in map:
        map[age] += 1
    else:
        map[age] = 1

map.pop(nanAge)




labels = list(map.keys())
sizes = list(map.values())


plt.pie(sizes,  labels=labels,shadow=True, startangle=90)


plt.show()



