from random import randint

def main(x : int, y : int):
    matriz = []

    for i in range(x):
        fila = []
        for j in range(y):
            try:
                num = int(input(f"Ingrese un valor para [{i}][{j}]: "))
                fila.append(num)
            except ValueError: 
                print("No se ingresó valor válido")
                fila.append(None)
        matriz.append(fila)

    return matriz

if __name__ == "__main__":
    matriz = main(x=100, y=100)
    [print(*fila) for fila in matriz]
    
