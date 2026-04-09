from random import randint
import numpy as np

def ejercicio_uno():
    vector = []
    for i in range(5): vector.append(int(input(f"Ingrese el número {i+1}: ")))
    return vector[::-1]
    
def ejercicio_dos():
    notas = []
    for i in range(6): notas.append(int(input(f"Ingrese la nota {i+1}: ")))
    return f"Promedio: {(sum(notas)/6)}", *notas

def ejercicio_tres():
    vector = []
    for _ in range(6): vector.append(int(input("Ingrese un número: ")))

    while True:
        numero_a_buscar = int(input("Ingrese un número a buscar: "))
        try: 
            num = vector.index(numero_a_buscar)
            print(f"{vector[num]} Sí está en la lista")
            break
        except ValueError: 
            print("No se encontró un número")
            
def ejercicio_cuatro():
    vector = []

    for _ in range(10): vector.append(
        # int(input("Ingrese un número: "))
        randint(-10,10)
        )
    
    pos = [num for num in vector if num > 0]
    neg = [num for num in vector if num < 0]

    return {
        "vector": vector,
        "nums": {
            "positivos": pos,
            "negativos": neg
        }

    }

def ejercicio_cinco():
    vector = []

    for _ in range(10): vector.append(
        # int(input("Ingrese un número: "))
        randint(-10,10)
        )

    pares = [num for num in vector if num % 2 == 0]
    impares = [num for num in vector if num % 2 != 0]

    return(pares, impares)

def ejercicio_seis(x: int, y: int):
    matriz = []
    numero_mayor = [0, [0, 0]]
    for i in range(x):
        fila = []
        for j in range(y):
            num = int(randint(-100, 1000)) # input("Ingrese un número: ")
            if num > numero_mayor[0]: 
                numero_mayor[0] = num
                numero_mayor[1][0] = i
                numero_mayor[1][1] = j
            fila.append(num)
        matriz.append(fila)

    return {
        "matriz": [fila for fila in matriz],
        "num_mayor": {
            "valor": numero_mayor[0],
            "fila": numero_mayor[1][0],
            "columna": numero_mayor[1][1]
        }
    }

def ejercicio_siete(x: int, y: int):
    matriz = []
    nums_mayores_50 = []

    for _ in range(x):
        fila = []
        for _ in range(y):
            num = int(randint(1, 100))
            if num > 50: nums_mayores_50.append(num)
            fila.append(num)
        matriz.append(fila)

    return matriz, nums_mayores_50

def ejercicio_ocho(dimension: int):
    """
    Para efectos de rapidez y testing se pusieron números aleatorios, reemplazar la linea de código 
    `int(input(f"Valor [{i}][{j}]: "))` por `randint(-100, 100)` para que pueda solicitar datos
    """
    matriz = [[randint(-100, 100) for j in range(dimension)] for i in range(dimension)]
    diagonal = [int(matriz[i][i]) for i in range(dimension)]

    return {
        "Matriz": matriz,
        "Diagonal": diagonal
    }

def ejercicio_nueve(x: int, y: int):
    matriz = [[randint(0, 1000) for j in range(y)] for i in range(x)]
    numeros_mayores_por_fila = []

    for fila in matriz:
        num_mayor = 0
        for num in fila:
            if num > num_mayor: num_mayor = num
        numeros_mayores_por_fila.append(num_mayor)
    
    return matriz, numeros_mayores_por_fila
        
def ejercicio_diez(x: int, y: int):
    matriz = [[randint(0, 20) for j in range(y)] for i in range(x)]
    numeros_mayores_10 = []

    for fila in matriz:
        num_mayores_10 = []
        for num in fila:
            if num >= 10: numeros_mayores_10.append(num)
        if num_mayores_10: numeros_mayores_10.append(num_mayores_10)
    
    return matriz, numeros_mayores_10

def ejercicio_propio(x: int, y: int):
    matriz = [[randint(0,1000) for j in range(y)] for i in range (x)]
    numeros_pares = []

    for fila in matriz:
        for num in fila:
            if num % 2 == 0: numeros_pares.append(num)

    return matriz, numeros_pares

print(ejercicio_propio(6,6))