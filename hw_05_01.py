file = open("file1.txt", "w")
text_input = None
while text_input != '':
    text_input = input('Введите данные (для выхода оставте поле пустым): ')
    file.write(text_input + '\n')
file.close()
