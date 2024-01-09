import random
num = 0
counter = 0
while counter != 7:
    counter = random.randint(1,10)
    num += 1

    print(num,".", counter, sep="")