import csv

filmMap = {

}
with open ('titles.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile, delimiter = ',')
    for row in reader:
        filmMap.setdefault(row['title'],[])
        filmMap[row['title']].append(row['imdb_score'])
        filmMap[row['title']].append(row['id'])
actorsTitles = {

}
with open ('credits.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile, delimiter = ',')
    for row in reader:
        if row['role'] == 'ACTOR':
           actorsTitles.setdefault(row['name'],[])
           actorsTitles[row['name']].append(row['id'])


#for title in titles:

sorted_values = sorted(filmMap.values())
newFilmMap = {

}

for value in sorted_values:
    for key in filmMap.keys():
        if filmMap[key] == value:
            newFilmMap[key] = filmMap[key]
            break



j = 0
invertedFimlMap = {}

for key, value in reversed(newFilmMap.items()):
    if (len(invertedFimlMap) < 1000):
        invertedFimlMap[key] = value
    else:
        break

topActors = {

}

for actor, valueActor in actorsTitles.items():
    for value in invertedFimlMap.values():
        if value[1] in valueActor:
            if actor in topActors.keys():
                topActors[actor] += 1
            elif actor not in topActors.keys():
                topActors[actor] = 1

sorted_actors = sorted(topActors.values())
newTopActors = {

}

for value in sorted_actors:
    for key in topActors.keys():
        if topActors[key] == value:
            newTopActors[key] = topActors[key]

invertedTopActors = {

}

for key, value in reversed(newTopActors.items()):
    if (len(invertedTopActors) < 10):
        invertedTopActors[key] = value
    else:
        break

print(invertedTopActors)
