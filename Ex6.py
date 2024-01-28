number = str(input('Ticket: '))
first_sum = 0
second_sum = 0
for i in number[0:3]:
    first_sum += int(i)

for n in number[3:6]:
    second_sum += int(n)


if first_sum == second_sum:
    print("Happy")
else:
    print("Ordinary")