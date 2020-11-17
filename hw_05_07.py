import json

d = {}
profit_sum = 0
with open("file7.txt") as file:
    b = sum(1 for _ in file)
with open("file7.txt") as file:
    for line in file:
        a = line.split()
        profit = int(a[2]) - int(a[3])
        if profit > 0:
            profit_sum = profit_sum + profit
        d.update({a[0]: profit})
spisok = [d, {'average_profit': (profit_sum / b)}]

with open('file7.json', 'w') as write_file:
    json.dump(spisok, write_file)
