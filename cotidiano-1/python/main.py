def primer_ejercicio():
    nums = []
    n = 0
    while n < 7:
        num = int(input("Ingrese un número: "))
        nums.append(num)
        n = n + 1
    return print("La suma es: ",sum(nums))

def segundo_ejercicio():
    num = []
    for i in range(1,101):
        if i % 2 == 0: num.append(i)

    return print(sum(num))

def tercer_ejercicio():
    return print((2023 - 1960) // 4 + 1) 

def cuarto_ejercicio():
    n = 3
    while n <= 90:
        if n % 3 == 0: print(n)
        n = n + 3
        
def quinto_ejercicio():
    n = 100
    while n != 0:
        print(n)
        n = n - 1 

def sexto_ejercicio(num : int):
    n = 1
    while n <= num:
        if n % 2 == 0: print(n)
        n = n + 1

def septimo_ejercicio():
    lista_nums = []
    n = 0
    while n < 5:
        num = int(input("Ingrese un número: "))
        lista_nums.append(num)
        n = n + 1

    return print(sum(lista_nums)/5)

def octavo_ejercicio():
    mujeres = 0
    hombres = 0

    i = int(input("Ingrese la cantidad: "))
    j = 0

    while j < i:
        op = input("Ingrese un opción: \n a) Hombre\n b) Mujer \n")
        op = op.lower()
        match op:
            case "a" | "hombre": 
                hombres = hombres + 1
                j = j + 1

            case "b" | "mujer": 
                mujeres = mujeres + 1
                j = j + 1

            case _: print("Ingrese un valor válido")
    
    return print((hombres / i) * 100, (mujeres / i) * 100)

def noveno_ejercicio():
    num = int
    nums = [0,0]
    while num != 0:
        num = int(input("Ingrese un número: "))
        if num > 0: nums[0] = nums[0] + 1
        elif num < 0: nums[1] = nums[1] + 1
    return print(f"Positivos: {nums[0]}\nNegativos: {nums[1]}")

def decimo_ejercicio():
    producto = int(input("Ingrese un número: "))
    n = 1
    while n <= 10:
        print(f"{producto} x {n} = {producto * n}")
        n = n + 1
    


# LlAMADAS A FUNCIONES

# primer_ejercicio()
# segundo_ejercicio()
# tercer_ejercicio()
# cuarto_ejercicio()
# quinto_ejercicio()
# sexto_ejercicio(int(input("Ingrese un número: ")))
# septimo_ejercicio()
# octavo_ejercicio()
# noveno_ejercicio()
decimo_ejercicio()