import io

fname = "file2.txt"
summa = 0
num_lines = 0
with io.open(fname, encoding='utf-8') as f:
    for line in f:
        words = line.split()
        if (int(words[1])) < 20000:
            print(words)
        summa = int(words[1]) + summa
        num_lines += 1
print(f'Средняя величина дохода сотрудников {summa / num_lines:.2f}')
