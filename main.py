import random
import threading

# Функция для генерации случайных матриц заданного размера
def generate_matrix(size):
    return [[random.randint(0, 9) for _ in range(size)] for _ in range(size)]

# Функция, которая будет выполняться в каждом потоке
def multiply_rows(matrix1, matrix2, result, row):
    size = len(matrix1)
    for col in range(size):
        for i in range(size):
            result[row][col] += matrix1[row][i] * matrix2[i][col]

# Запрашиваем размер матриц у пользователя
size = int(input("Введите размер матриц: "))

# Генерируем две матрицы случайных чисел
matrix1 = generate_matrix(size)
matrix2 = generate_matrix(size)

# Создаем матрицу-результат и заполняем её нулями
result = [[0 for _ in range(size)] for _ in range(size)]

# Создаем список потоков
threads = []

# Запускаем каждый поток, чтобы каждый поток выполнял умножение строк матрицы 1 на матрицу 2
for row in range(size):
    thread = threading.Thread(target=multiply_rows, args=(matrix1, matrix2, result, row))
    thread.start()
    threads.append(thread)

# Ждем, пока все потоки завершатся
for thread in threads:
    thread.join()

# Выводим исходные матрицы и матрицу-результат
print("Матрица 1:")
for row in matrix1:
    print(row)

print("Матрица 2:")
for row in matrix2:
    print(row)

print("Результат умножения матриц:")
for row in result:
    print(row)
