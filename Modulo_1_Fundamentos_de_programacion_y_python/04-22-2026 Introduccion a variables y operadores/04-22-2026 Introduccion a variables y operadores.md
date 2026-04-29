# 📘 FUNDAMENTOS DE PROGRAMACIÓN Y PYTHON

## 🧠 CLASE 2: Variables, Operadores y Tipos de Datos

---

## 🔹 Variables

* Se utilizan para almacenar información en memoria.
* Se pueden renombrar, pero es importante seguir convenciones claras.

### 📌 Ejemplo

```python
# Variable declaration
name = "Ana"
age = 25
height = 1.68
is_student = True

# Show values
print(name, age, height, is_student)
print(type(name), type(age), type(height), type(is_student))
```

---

## ⚠️ Errores comunes

### ❌ 1. Usar una variable sin definir

```python
print(name)
```

---

### ❌ 2. Sobrescribir funciones built-in

```python
print = 'hola'
print("hello")

del print
```

---

## ✨ f-strings (forma profesional de imprimir)

```python
name = "Jose"
age = 26

print(f"Hola, mi nombre es {name} y tengo {age} años.")
```

---

## 📊 Tipos de datos en Python

* **int** → enteros (`10`, `-5`)
* **float** → decimales (`3.14`)
* **str** → texto (`"Hola"`)
* **bool** → booleanos (`True`, `False`)

### 📌 Ver tipos

```python
print(type(name))      # str
print(type(age))       # int
print(type(height))    # float
print(type(is_student))# bool
```

---

## ⌨️ Entrada de datos y casting

```python
user_data = input("Dime un número para multiplicar por 2: ")

n = int(user_data)

print(f"El resultado es: {n * 2}")
```

---

## ➕ Operadores Aritméticos

```python
a = 12
b = 3

print("Suma:", a + b)
print("Resta:", a - b)
print("Multiplicación:", a * b)
print("División:", a / b)
print("División entera:", a // b)
print("Módulo:", a % b)
print("Exponente:", a ** b)
```

---

### ❌ Error: división por cero

```python
a = 10
b = 0
print(a / b)
```

---

## 🔍 Operadores de Comparación

```python
x = 3
y = 4
z = 2

print(x == y)
print(x != y)
print(x > y)
print(x <= y)
print(x < y < z)
```

---

## 🔗 Operadores Lógicos

```python
a = True
b = False

print(a and b)
print(a or b)
print(not a)
```

---

## ⚡ Booleanos en Python

```python
print(False == 0)
print(True == 1)
print(True == 2)

print(False + True)
print(True * 10)
```

---

## 🔤 Operaciones con Strings

```python
print("hola" * 3)
print("Hola " + "Mundo")
```

---

## 🎟️ Ejercicio: Entrada de cine

```python
age = int(input("Introduce tu edad: "))
input_tarjeta = input("¿Eres cliente? (si/no): ")

tarjeta_cliente = (input_tarjeta == "si")

descuento = age <= 12 or age >= 65 or tarjeta_cliente

precio = 14

print("¿Tienes descuento?", descuento)
print("Precio final:", precio * (1 - (0.5 * descuento)))
```

---

## ⚠️ Error típico

```python
print("Tengo" + 25 + "años")
```

---

## 🧹 Métodos de String

```python
correo = "   USUARIO@GMAIL.COM   "

print(correo.strip())
print(correo.strip().lower())
```

```python
name = "paula rodríguez simón"

print(name.upper())
print(name.capitalize())
print(name.title())
```

---

## 💡 Buenas prácticas

* Python distingue mayúsculas y minúsculas
* Evitar palabras reservadas
* Usar nombres descriptivos

```python
temperatura_celsius = 22.5
esta_nublado = False

print("Temperatura:", temperatura_celsius)
print("¿Está nublado?", esta_nublado)
```

---

## 🧪 Retos finales

### 🧮 Reto 1: IMC

```python
height = float(input("Altura en cm: "))
weight = float(input("Peso en kg: "))

imc = weight / (height / 100) ** 2

print(f"Tu IMC es: {imc:.2f}")
```

---

### 🧠 Reto 2: Analizador de nombres

```python
nombre = input("Escribe tu nombre completo: ")

contador = len(nombre.replace(" ", ""))

print(f"Tu nombre {nombre.title()} tiene {contador} letras")
```

---
