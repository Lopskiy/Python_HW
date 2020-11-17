import io

fr = "file6.txt"

d = {}
with io.open(fr, encoding='utf-8') as file:
    for line in file:
        key, *value = line.split()
        d[key] = value #Физика Лекции 10 Практика 20 Лабораторная 4

print(d)
