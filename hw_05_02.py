fname = "file1.txt"

num_lines = 0
num_words = 0

with open(fname, 'r') as f:
    for line in f:
        words = line.split()

        num_lines += 1
        num_words += len(words)

print(f'Колличество строк в файле: {num_lines}\nКолличество строк в файле: {num_words}')
