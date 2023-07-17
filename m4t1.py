import random

file = open('data.txt', 'w')

#my_list = [int(i) for i in file]

for _ in range(10000):
    num = random.randint(1,10000)
    file.write(str(num) + '\n')

file.close()
