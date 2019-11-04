class Date:
    @classmethod
    def chislo(cls, date_str):
        for el in map(int, date_str.split("-")):
            print(f'Элемент-{el} Тип-{type(el)}')

    @staticmethod
    def valid(date_str):
        s = list(map(int, date_str.split("-")))
        if 1 < s[0] < 31 and 1 < s[1] < 12 and 2000 < s[2] < 2050:
            print('All good!')
        else:
            print('Bad date')


Date.chislo('20-10-2019')
Date.valid('20-10-2019')
