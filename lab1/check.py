import numpy as np

matrix1 = "C:/Parallel-programing/lab1/matrix1.txt"
matrix2 = "C:/Parallel-programing/lab1/matrix2.txt"
endfile = "C:/Parallel-programing/lab1/endfile.txt"

def load_square_matrix(filename):
    with open(filename, 'r') as f:
        n = int(f.readline().strip())
        matrix = np.loadtxt(f, max_rows=n)
        return matrix

print("Загрузка матриц...")
A = load_square_matrix(matrix1)
B = load_square_matrix(matrix2)

result_numpy = np.dot(A, B)

print("Проверка корректности умножения...")
loaded_result = load_square_matrix(endfile)

if np.allclose(result_numpy, loaded_result):
    print("Результаты совпадают!")
else:
    print("Ошибка: результаты не совпадают!")