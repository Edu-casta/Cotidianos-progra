def main():
    # Solicitar números
    cantidad_nums = int(input("¿Cuántos números desea ingresar?: "))
    data = [0,0,0,0,0,0,0,0] # pos, neg, pares, impa, mayor, menor, suma, prom
    if cantidad_nums <= 0:
        return None


    for _ in range(cantidad_nums):
        num = int(input("Ingrese un número: "))
        if num > 0: data[0] += 1 
        else: data[1] += 1

        if num % 2 == 0: data[2] += 1
        else: data[3] += 1

        if num > data[4]: data[4] = num
        if num < data[5]: data[5] = num

        data[6] += num

    return data, cantidad_nums


if __name__ == "__main__":
    resultado = main()

    if resultado:
        data, total = resultado
        print(f"""
Números ingresados: {total}
Números positivos: {data[0]}
Números negativos: {data[1]}
Números pares: {data[2]}
Números impares: {data[3]}
Número mayor: {data[4]}
Número menor: {data[5]}
Promedio: {data[6] / total}
""")
        
    else:
        print("No se ingresaron números")
