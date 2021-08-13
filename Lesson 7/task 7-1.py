class Matrix:

    def __init__(self, spisok_spiskov):
        self.matrix = spisok_spiskov

    def __str__(self):
        res = ""
        for spisok in self.matrix:
            for el in spisok:
                res += f"{el:>5}"
            res += "\n"
        return res

    def __add__(self, other):
        razm = True
        if len(self.matrix) != len(other.matrix):
            razm = False
        for i, spisok in enumerate(self.matrix, 0):
            if len(spisok) != len(other.matrix[i]):
                razm = False
        if razm:
            new_matr = []
            for i in range(len(self.matrix)):
                new_line = []
                for j in range(len(self.matrix[i])):
                    new_line.append(self.matrix[i][j] + other.matrix[i][j])
                new_matr.append(new_line)
            return Matrix(new_matr)
        else:
            print("Размерность матриц не совпадает!")
            return None

my_matr = Matrix([[1,2,3],[4,5,6],[7,8,9]])
my_matr2 = Matrix([[1,0,0],[0,1,0],[0,0,1]])
print(my_matr)
print(my_matr2)
print(my_matr + my_matr2)
