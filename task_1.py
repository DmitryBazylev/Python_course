city_list = [
    {"city": "Москва", "population": 12.5},
    {"city": "Санкт-Петербург", "population": 5.4},
    {"city": "Москва", "population": 1.6},
    {"city": "Екатеринбург", "population": 1.5},
    {"city": "Нижний Новгород", "population": 1.3},
]

num_cities = len(city_list)  # TODO найдите количество городов в списке

list = city_list[1]
t=0
for popul in city_list:
    t+=popul["population"]
print(t)
total_population = t  # TODO найдите общее количество населения

print(num_cities, list["population"])

print(f"Среднее арифметическое населения равно = {t/len(city_list)}")  # TODO распечатайте среднее арифметическое населения
