import io

fr = "file3.txt"
fo = "file4.txt"
i = 0
translate = ['Один', 'Два', 'Три', 'Четыре']

with io.open(fr, encoding='utf-8') as f_r:
    for line in f_r:
        words = line.split()
        words.pop(0)
        words.insert(0, translate[i])
        i += 1
        with open(fo, 'a') as f_w:
            f_w.writelines(' '.join(words) + '\n')
print(words)
