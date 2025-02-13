def sumar_matrices(A, B):
    filas = len(A)
    columnas = len(A[0])
    resultado = []
    for i in range(filas):
        fila = []
        for j in range(columnas):
            fila.append(A[i][j] + B[i][j])
        resultado.append(fila)
    return resultado

def multiplicar_matrices(A, B):
    filas_A = len(A)
    columnas_A = len(A[0])
    filas_B = len(B)
    columnas_B = len(B[0])
    
    if columnas_A != filas_B:
        return None  # No se pueden multiplicar
    
    resultado = [[0 for _ in range(columnas_B)] for _ in range(filas_A)]
    for i in range(filas_A):
        for j in range(columnas_B):
            for k in range(columnas_A):
                resultado[i][j] += A[i][k] * B[k][j]
    return resultado

if __name__ == '__main__':
    # Ejemplo de matrices para sumar
    A = [
        [1, 2, 3],
        [4, 5, 6]
    ]
    B = [
        [7, 8, 9],
        [10, 11, 12]
    ]
    
    print("Matriz A:")
    for fila in A:
        print(fila)
    print("Matriz B:")
    for fila in B:
        print(fila)
    
    # Suma de matrices
    if len(A) == len(B) and len(A[0]) == len(B[0]):
        suma = sumar_matrices(A, B)
        print("Suma de A y B:")
        for fila in suma:
            print(fila)
    else:
        print("No se pueden sumar matrices de dimensiones diferentes.")
    
    # Multiplicación de matrices
    # Para multiplicar, se usa otra matriz C compatible: A (2x3) * C (3x2)
    C = [
        [1, 2],
        [3, 4],
        [5, 6]
    ]
    producto = multiplicar_matrices(A, C)
    if producto is not None:
        print("Producto de A y C:")
        for fila in producto:
            print(fila)
    else:
        print("No se pueden multiplicar las matrices con las dimensiones dadas.")
