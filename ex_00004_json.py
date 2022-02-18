import json
# dump - сохранение объекта в формате json в файл
# dumps - преобразование объекта в json (в текст)
# load - загрузка объекта из файла
# loads - загрузка объекта из формата json (строки)

friends = [
    {'name': 'Max', 'age': 23, 'phones': [123, 345]},
    {'name': 'Leo', 'age': 33}
]
# посмотрим тип объекта
print(type(friends))

# преобразуем в json
# json_friends = json.dumps(friends)
# # печатаем что получилось
# print(json_friends)
# # проверим тип
# print(type(json_friends))

# запишем в файл
with open('friends.json', 'w') as f:
    json_friends = json.dump(friends, f)


# обратно из json в объект
# friends = json.loads(json_friends)

# обратно из файла в объект
with open('friends.json', 'r') as f:
    friends = json.load(f)
print(friends)
print(type(friends))

favourite_tracks = [
    {'name': 'Фигня 1', 'artist': 'агата Кристи'},
    {'name': 'Angel', 'artist': 'Massive Attack'},
    {'name': 'Jamming', 'artist': 'Bob Marley'}
]

with open('track.json', 'w', encoding='utf-8') as f:
    json.dump(favourite_tracks, f)

print('Выполнено')