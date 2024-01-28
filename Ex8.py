correct_numbers = []

while True:
    n = int(input("Number: "))
    if n < 12:
        continue
    elif n > 100:
        break
    else:
        correct_numbers.append(n)

for i in correct_numbers:
    print(i)