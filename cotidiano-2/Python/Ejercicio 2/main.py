from pydantic import BaseModel, ValidationError
from fastapi import FastAPI, status, HTTPException
import json

app = FastAPI()

class Usuario(BaseModel):
    name: str
    password: str
    tier: str
    credits: float
    inventory: list

class Producto(BaseModel):
    name: str
    price: float
    stock: int

# Consistencia
USERS_FILE = "usuarios.json"
PRODUCTS_FILE = "productos.json"

def save(file, data):
    with open(file, "w", encoding="utf-8") as f:
        json.dump(data, f, indent = 4)

def load(file):
    with open(file, "r", encoding="utf-8") as f:
        return json.load(f)

# Lógica de negocio
@app.put("/user")
def registrar(name: str, password: str, tier: str):
    try:
        new_user = Usuario(name=name, password=password, tier=tier, credits=0.0, inventory=[])
        users_list = load(USERS_FILE)

        if any(name == u["name"] for u in users_list): return "Usuario ya existente"

        users_list.append(new_user.model_dump())
        save(USERS_FILE, users_list)
        return "success"
    except ValidationError as e:
        return f"Error: {e}"
    
@app.put("/creditos")
def modificar_creditos(nombre: str, password: str, credits: float):
    try:
        users_list = load(USERS_FILE)
        for u in users_list:
            if u["name"] == nombre and u["password"] == password:
                u["credits"] += credits
                save(USERS_FILE, users_list)
                return {
                    "status": status.HTTP_202_ACCEPTED,
                    "data": {
                        "user_name": u["name"],
                        "user_credits": u["credits"]
                    }
                }
        raise ValidationError
    except ValidationError as e:
        return f"Error: {e}"

@app.get("/producto")
def comprar_producto(product_name: str, product_amount: int, user_name: str, user_pass: str):
    try:
        user_list = load(USERS_FILE)
        product_list = load(PRODUCTS_FILE)

        # Validación de usuario
        found_user = next((u for u in user_list if u["name"] == user_name and u["password"] == user_pass), None)
        found_product = next((p for p in product_list if p["name"] == product_name), None)

        if not (found_user or found_product): raise HTTPException(status.HTTP_404_NOT_FOUND, detail="Credenciales incorrectas")

        # Lógica de compra
        discount = 0
        if found_user["tier"].lower() == "cliente frequente": discount = 0.10
        if found_user["tier"].lower() == "vip": discount = 0.20

        price = (found_product["price"] * product_amount) - (found_product["price"] * discount)
        if found_user["credits"] < price: raise HTTPException(status.HTTP_400_BAD_REQUEST, detail="Fondos insuficientes")
        if product_amount > found_product["stock"]: raise HTTPException(status.HTTP_400_BAD_REQUEST, "No hay stock disponible")

        found_user["credits"] -= price
        found_product["stock"] -= product_amount

        # Inventario
        # [{"name": amount}, {"name": amount}, ...]
        inventory = found_user["inventory"]
        found_item = next((item for item in inventory if item.keys() == found_product["name"]), None)

        # Si el usuario ya tiene un producto
        if found_item: found_item["name"] += product_amount

        # El usuario no tiene el producto
        else: 
            new_item = {found_product["name"]: product_amount}
            inventory.append(new_item)

        save(USERS_FILE, user_list)
        save(PRODUCTS_FILE, product_list)

        return "success"

    except ValidationError as e:
        return f"Error: {e}"

@app.post("/producto", status_code=status.HTTP_201_CREATED)
def añadir_producto(name: str, price: float, stock: int):
    try:
        products_list = load(PRODUCTS_FILE)

        # Encontrar producto, usar next para encontrar la primera conincidencia y terminar el bucle
        found_product = next((p for p in products_list if p["name"] == name), None)

        # Si hay producto
        if found_product: found_product["stock"] += stock

        # añadir producto
        else: 
            new_product = Producto(name=name, price=price, stock=stock)
            products_list.append(new_product.model_dump())


        save(PRODUCTS_FILE, products_list)
        return {
            "status": 201
        }
    except ValidationError as e:
        return f"Error: {e}"

load(PRODUCTS_FILE)
load(USERS_FILE)