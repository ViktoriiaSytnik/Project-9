import csv
import numpy as np
titles = []
with open ('titles.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile, delimiter = ',')
    for row in reader:
        titles.append(row)
def sort_fn(row):

    return row['imdb_score']

titles.sort(key = sort_fn)
titles = titles[0:1000]

actors = []
with open ('credits.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile, delimiter = ',')
    for row in reader:
        if row['role'] == 'ACTOR':
           actors.append(row)

title_ids = {}
for title in titles:
    title_ids[title['id']] = True

actor_popularity = {}
for actor in actors:
    if actor['id'] in title_ids:
        if actor['name'] in actor_popularity:
            actor_popularity[actor['name']] += 1
        else:
            actor_popularity[actor['name']] = 1
result = []
for key,value in actor_popularity.items():
    result.append([key,value])
def sort_rs(row):
    return row[1]
result.sort(key= sort_rs,reverse=True)
result = result[0:10]

mapped_res = []
for row in result:
    mapped_res.append(row[0])

arr_1 = np.array(mapped_res)
list_1 = arr_1.tolist()
print(f'TOP-10: 1.{list_1[0]}, 2.{list_1[1]}, 3.{list_1[2]}, 4.{list_1[3]}, 5.{list_1[4]}, 6.{list_1[5]}, 7.{list_1[6]}, 8.{list_1[7]}, 9.{list_1[8]}, 10.{list_1[9]}')










