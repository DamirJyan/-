import numpy as np

def gauss_inverse(matrix):
    n = len(matrix)
    augmented_matrix = np.concatenate((matrix, np.identity(n)), axis=1)

    print("Исходная матрица A:")
    print(matrix)

    for i in range(n):
        max_index = i
        max_value = augmented_matrix[i, i]
        for j in range(i+1, n):
            if augmented_matrix[j, i] > max_value:
                max_index = j
                max_value = augmented_matrix[j, i]
        augmented_matrix[[i, max_index]] = augmented_matrix[[max_index, i]]
        
        if augmented_matrix[i, i] == 0:
            print("Матрица A является вырожденной. Обратной матрицы не существует.")
            return None
        
        augmented_matrix[i] = augmented_matrix[i] / augmented_matrix[i, i]
        
        print("Преобразование " + str(i+1) + ":")
        print(np.around(np.concatenate((np.identity(n), augmented_matrix[:, n:]), axis=1), decimals=decimals))
        
        for j in range(n):
            if j != i:
                augmented_matrix[j] = augmented_matrix[j] - augmented_matrix[j, i] * augmented_matrix[i]
    
    inverse_matrix = augmented_matrix[:, n:]
    
    return inverse_matrix

# Выбор режима ввода матрицы
mode = input("Выберите способ ввода матрицы:\n1. Сгенерировать случайную матрицу\n2. Ввести матрицу вручную\nВведите число: ")

# Генерация случайной матрицы
if mode.lower() == "1":
    # Ввод размерности матрицы с клавиатуры
    n = int(input("Введите размерность матрицы A: "))
    
    # Генерация случайной матрицы с целыми числами
    matrix = np.random.randint(low=1, high=10, size=(n, n))
    
    print("Сгенерированная матрица A:")
    print(matrix)

# Ввод матрицы вручную
elif mode.lower() == "2":
    # Ввод размерности матрицы с клавиатуры
    n = int(input("Введите размерность матрицы A: "))
    
    # Ввод элементов матрицы с клавиатуры
    print("Введите элементы матрицы A:")
    matrix = np.zeros((n, n), dtype=float)
    for i in range(n):
        for j in range(n):
            matrix[i, j] = float(input("Элемент [" + str(i+1) + ", " + str(j+1) + "]: "))
    
else:
    print("Некорректный выбор режима.")
    exit()

decimals = int(input("Введите количество знаков после запятой для вывода матрицы: "))

inverse = gauss_inverse(matrix)

if inverse is not None:
    print("Обратная матрица A^(-1):")
    print(np.around(inverse, decimals=decimals))