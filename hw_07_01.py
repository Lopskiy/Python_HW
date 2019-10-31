class Matrix():
    def __init__(self, list_of_lists):
        self.mat = list_of_lists

    def str(self):
        string = ''
        for i in self.mat:
            for j in i:
                string = string + '%s\t' % (j)
            string = string[:-1]
            string = string + '\n'
        string = string[:-1]
        return string

    def __add__(self, other):
        try:
            result = []
            numbers = []
            for i in range(len(self.mat)):
                for j in range(len(self.mat[0])):
                    summa = other.mat[i][j] + self.mat[i][j]
                    numbers.append(summa)
                    if len(numbers) == len(self.mat):
                        result.append(numbers)
                        numbers = []
            return Matrix(result)
        except IndexError:
            print('Матрицы должны быть одинакового размера')


a = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
b = [[-10, 8, 7], [-6, 5, 4], [0, 4, 7]]
m1 = Matrix(a)
m2 = Matrix(b)
print(f'{m1.str()} \n{m2.str()}')
m3 = m1 + m2
print(f'{m3.str()}')
