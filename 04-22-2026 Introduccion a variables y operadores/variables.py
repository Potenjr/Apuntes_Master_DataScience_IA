
# 📘 variables.py
# Ejercicio completo - Variables, tipos de datos y operadores

# -------------------------------
# 1. Datos del usuario (input)
# -------------------------------

nombre = input("¿Cómo te llamas? ")
edad = int(input("¿Cuántos años tienes? "))
altura = float(input("¿Cuánto mides en cm? "))
input_tarjeta = input("¿Tienes tarjeta de cliente? (si/no): ")

# Convertimos a booleano
tiene_tarjeta = input_tarjeta.lower() == "si"

print("\n--- DATOS INTRODUCIDOS ---")
print(f"Nombre: {nombre}")
print(f"Edad: {edad}")
print(f"Altura: {altura} cm")
print(f"Tarjeta cliente: {tiene_tarjeta}")

# -------------------------------
# 2. Tipos de datos
# -------------------------------

print("\n--- TIPOS DE DATOS ---")
print(type(nombre))
print(type(edad))
print(type(altura))
print(type(tiene_tarjeta))

# -------------------------------
# 3. Operaciones básicas
# -------------------------------

print("\n--- OPERACIONES ---")

# Aritméticas
print("Edad en 5 años:", edad + 5)
print("Altura en metros:", altura / 100)

# Comparaciones
es_mayor = edad >= 18
print("¿Es mayor de edad?", es_mayor)

# Lógicos
descuento = edad <= 12 or edad >= 65 or tiene_tarjeta
print("¿Tiene descuento?", descuento)

# -------------------------------
# 4. Ejercicio cine
# -------------------------------

precio = 14
precio_final = precio * (1 - (0.5 * descuento))

print(f"Precio final de la entrada: {precio_final}€")

# -------------------------------
# 5. Strings
# -------------------------------

print("\n--- FORMATO DE TEXTO ---")

print("Nombre en mayúsculas:", nombre.upper())
print("Nombre capitalizado:", nombre.capitalize())
print("Nombre tipo título:", nombre.title())

# Contar letras (sin espacios)
letras = len(nombre.replace(" ", ""))
print(f"Tu nombre tiene {letras} letras (sin espacios)")

# -------------------------------
# 6. Extra: IMC
# -------------------------------

peso = float(input("\nIntroduce tu peso en kg: "))

imc = peso / (altura / 100) ** 2

print(f"Tu IMC es: {imc:.2f}")

# -------------------------------
# 7. Mensaje final
# -------------------------------

print("\n--- RESUMEN FINAL ---")
print(f"{nombre.title()}, tienes {edad} años, mides {altura} cm y tu IMC es {imc:.2f}")

