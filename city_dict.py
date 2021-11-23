#задание 1

from pprint import pprint

city_dict = {
    "city": "Moscow",
    "temperature": "20"
}
print(city_dict["city"])
city_dict["temperature"] = "15"
pprint(city_dict)

#задание 2

print(city_dict.get('country', 'Россия'))
city_dict ["date"] = "27.05.2019"
print(len(city_dict))

