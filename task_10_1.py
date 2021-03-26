class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix

    def __str__(self):
        return '\n'.join(map(str, self.matrix))

    def __add__(self, other):
        final_matrix = []
        for i in range(len(self.matrix)):
            final_matrix.append([])
            for j in range(len(self.matrix[0])):
                final_matrix[i].append(self.matrix[i][j] + other.matrix[i][j])
        return '\n'.join(map(str, final_matrix))


matrix_1 = Matrix([[1, 2, 5], [4, 5, 6], [7, 8, 8]])
matrix_2 = Matrix([[9, 10, 6], [12, 45, 5], [1, 2, 5]])
print(matrix_1)
print(matrix_2)
print(matrix_1 + matrix_2)
