from fastapi import FastAPI, HTTPException, status

app = FastAPI()

@app.get("/")
def home():
    return "Entrar a http://127.0.0.1:8000/docs"

@app.get("/ejercicio-1", status_code=200)
def ejercicio_1(num1: int | float, num2: int | float, num3: int | float):
    return num1 + num2 + num3

@app.get("/ejercicio-2", status_code=200)
def ejercicio_2(num1: int | float, num2: int | float, num3: int | float, op : str = ""):
    op = op.lower()
    nums = [num1, num2, num3]
    match op:
        case "+": return(sum(nums))
        case "-": return num1 - num2 - num3
        case "*": return num1 * num2 * num3 
        case "/": 
            try: return num1 / num2 / num3 
            except ZeroDivisionError as e: return HTTPException(status.HTTP_500_INTERNAL_SERVER_ERROR, detail=f"ERROR: {e}")
        case "prom": return sum(nums) / len(sum)
        case _: return HTTPException(status_code=400)

@app.get("/ejercicio-3", status_code=200)
def ejercicio_3(calificacion_estudiante : int | float):
    if calificacion_estudiante < 0 or calificacion_estudiante > 100: return HTTPException(status_code=400)
    if calificacion_estudiante >= 90: return "A"
    if calificacion_estudiante >= 80: return "B"
    if calificacion_estudiante >= 70: return "C"
    if calificacion_estudiante >= 60: return "D"
    return "E"

# Se realiza en local ya que no permite ejecutarlo en la API
def ejercicio_4(cantidad_nums : int): 
    nums = [int(input("Ingrese un número: ")) for _ in range(cantidad_nums)]
    return sum(nums)

if __name__ == "__main__":
    print(ejercicio_4(int(input("¿Cuantos números desea ingresar? \n"))))

