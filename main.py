import random


numbers = []
while len(numbers) < 6:
    numbers.append(random.randint(1,10))


set_number = set(numbers)

while len(numbers) != len(set_number):
    x = random.randint(1,10)

    if x in set_number:
        pass
    else:
        set_number = list(set_number)
        set_number.append(x)

print (set_number)