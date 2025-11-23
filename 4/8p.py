import csv

with open('1.csv', 'r', encoding='utf-8') as file:
    data = list(csv.DictReader(file))

data_with_int_age =  list(map(lambda x: {
    'Имя': x['Имя'],
    'Возраст': int(x['Возраст']),
    'Должность': x['Должность']
}, data))

adults = list(filter(lambda x: x['Возраст'] > 25, data_with_int_age))

print("Сотрудники старше 25 лет:")
for person in adults:
    print(f"- {person['Имя']}, {person['Возраст']} лет, {person['Должность']}")
