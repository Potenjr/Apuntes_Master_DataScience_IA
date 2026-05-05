# =========================================
# CONDICIONALES Y BUCLES EN PYTHON
# =========================================

print("=== CONDICIONALES ===")

# Ejemplo básico
edad = int(input("Introduce tu edad: "))

if edad < 18:
    print("Eres menor de edad")
elif edad == 18:
    print("Tienes justo 18 años")
else:
    print("Eres mayor de edad")

# Operadores lógicos
tiene_dni = input("¿Tienes DNI? (si/no): ").lower()

if edad >= 18 and tiene_dni == "si":
    print("Puedes acceder")
else:
    print("No puedes acceder")

# =========================================
print("\n=== BUCLE FOR ===")

# Recorrer lista
numeros = [1, 2, 3, 4, 5]

for num in numeros:
    print("Número:", num)

# Range
print("\nContador con range:")
for i in range(1, 6):
    print(i)

# Pares e impares
print("\nNúmeros pares e impares:")
for i in range(10):
    if i % 2 == 0:
        print(i, "es par")
    else:
        print(i, "es impar")

# =========================================
print("\n=== BUCLE WHILE ===")

contador = 0

while contador < 5:
    print("Contador:", contador)
    contador += 1

# =========================================
print("\n=== BREAK Y CONTINUE ===")

# Break
for i in range(10):
    if i == 5:
        print("Se detiene el bucle")
        break
    print(i)

# Continue
for i in range(5):
    if i == 2:
        continue
    print("Valor:", i)

# =========================================
print("\n=== MINI PROGRAMA ===")

# Adivinar número
import random

numero_secreto = random.randint(1, 10)
intentos = 0

while True:
    intento = int(input("Adivina el número (1-10): "))
    intentos += 1

    if intento == numero_secreto:
        print(f"¡Correcto! Lo lograste en {intentos} intentos")
        break
    elif intento < numero_secreto:
        print("Más alto")
    else:
        print("Más bajo")