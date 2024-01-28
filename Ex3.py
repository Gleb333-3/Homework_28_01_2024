word_list = ["apple", "banana", "orange", "grape", "kiwi", "banana", "pear", "orange",
"orange", "mango", "pear", "banana", "kiwi", "mango", "watermelon",
"kiwi", "raspberry", "banana", "orange", "raspberry", "avocado", "kiwi", "pear", "raspberry"]

dictin = {}

for i in word_list:
    dictin.setdefault(i, word_list.count(i))
print(dictin)
