words = input('Введите слова через пробел: ')
i = 1

for split in words.split():
    print(i, split[:10])
    i = i + 1
