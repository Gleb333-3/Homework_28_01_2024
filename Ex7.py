n = int(input("N: "))

stringg = ''
number = 0
count = 0
while number <= n:
    count += 1
    number = count **2
    if number > n:
        break
    stringg += f"{str(number)} "

print(stringg)
