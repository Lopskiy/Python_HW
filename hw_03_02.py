def id_func(f_name, f_surname, f_year, f_city, f_email, f_tel):
    print('Имя:', f_name, 'Фамилия:', f_surname, 'Год рождения:', f_year, 'Город:', f_city, 'E-mail:', f_email, 'Тел:',
          f_tel)


id_func(f_name=input('Введите ваше имя '), f_surname=input('Введите вашу фамилию '),
        f_year=input('Введите ваш год рождения '), f_city=input('Введите ваш город '),
        f_email=input('Введите ваш email '), f_tel=input('Введите ваш телефон '))
