def adding_pair(dictionary, country, capital):
    return dictionary.setdefault(country, capital)

def deleting_items(dictionary, country):
    return dictionary.pop(country)

def searching_country(dictionary, country):
    for key in dictionary.keys():
        if key == country:
            return key

def searching_capital(dictionary, capital):
    for value in dictionary.values():
        if value == capital:
            return value


dictin = {"France": "Paris",
          "Germany": "Berlin",
          "Italy": "Rome"}


adding_pair(dictin, "Russia", "Moskow")
deleting_items(dictin, "Germany")
print(searching_country(dictin, "Russia"))
print(searching_capital(dictin, "Paris"))
print(dictin)