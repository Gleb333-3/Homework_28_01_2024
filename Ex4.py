dictin = {"Mark1:": 5, "Mark2:": 2,"Mark3:": 3,"Mark4:": 6, "Mark5:": 7}

keys = list(dictin)

dictin[keys[0]], dictin[keys[len(keys) - 1]] = dictin[keys[len(keys) - 1]], dictin[keys[0]]

dictin.pop(keys[1])

dictin.setdefault("Mark6", 9)

print(dictin)