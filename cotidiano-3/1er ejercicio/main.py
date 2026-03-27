def main(n: int):
    vector = []
    for i in range(n):
        vector.append(int(input(f"Ingrese el número {i+1}: ")))
    return vector

if __name__ == "__main__":
    num = int(input("Ingrese la cantidad de números que quiere ingresar: "))
    print(main(num))

    

