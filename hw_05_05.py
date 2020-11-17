import random

file = open("file5.txt", "r+")
for x in range(0, 10):
    file.write(f' {random.randint(0, 10)}')
    print(*(sum(map(int, line.split())) for line in file.readlines()))
file.close()



