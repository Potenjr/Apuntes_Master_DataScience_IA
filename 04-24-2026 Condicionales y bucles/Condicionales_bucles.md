# 📘 CONDICIONALES Y BUCLES EN PYTHON

---

## 🔹 1. Condicionales (`if`, `elif`, `else`)

Permiten tomar decisiones en el programa.

### 🧠 Sintaxis básica

```python
if condicion:
    # código
elif otra_condicion:
    # código
else:
    # código
```

### 📌 Ejemplo

```python
edad = 18

if edad < 18:
    print("Eres menor de edad")
elif edad == 18:
    print("Tienes justo 18 años")
else:
    print("Eres mayor de edad")
```

---

### 🔸 Operadores de comparación

* `==` → Igual
* `!=` → Distinto
* `>` → Mayor que
* `<` → Menor que
* `>=` → Mayor o igual
* `<=` → Menor o igual

---

### 🔸 Operadores lógicos

* `and` → Y
* `or` → O
* `not` → Negación

```python
edad = 20
tiene_dni = True

if edad >= 18 and tiene_dni:
    print("Puedes entrar")
```

---

### 🔸 Condicionales anidados

```python
nota = 7

if nota >= 5:
    print("Aprobado")
    if nota >= 9:
        print("Sobresaliente")
else:
    print("Suspenso")
```

---

## 🔹 2. Bucles

Permiten repetir código.

---

## 🔁 2.1 Bucle `for`

Se usa cuando sabes cuántas veces repetir.

### 📌 Sintaxis

```python
for variable in iterable:
    # código
```

### 📌 Ejemplo

```python
numeros = [1, 2, 3, 4, 5]

for num in numeros:
    print(num)
```

---

### 📌 Uso de `range()`

```python
for i in range(5):
    print(i)
```

👉 Salida: 0, 1, 2, 3, 4

```python
for i in range(1, 6):
    print(i)
```

👉 Salida: 1, 2, 3, 4, 5

---

### 🔸 Recorrer strings

```python
for letra in "Python":
    print(letra)
```

---

## 🔁 2.2 Bucle `while`

Se usa cuando no sabes cuántas repeticiones habrá.

### 📌 Sintaxis

```python
while condicion:
    # código
```

### 📌 Ejemplo

```python
contador = 0

while contador < 5:
    print(contador)
    contador += 1
```

---

⚠️ Cuidado con bucles infinitos:

```python
while True:
    print("Esto nunca para")
```

---

## 🔹 3. Control de bucles

### 🔸 `break`

Rompe el bucle.

```python
for i in range(10):
    if i == 5:
        break
    print(i)
```

---

### 🔸 `continue`

Salta una iteración.

```python
for i in range(5):
    if i == 2:
        continue
    print(i)
```

---

### 🔸 `pass`

No hace nada (placeholder).

```python
if True:
    pass
```

---

## 🔹 4. Condicionales + Bucles

```python
for i in range(10):
    if i % 2 == 0:
        print(i, "es par")
    else:
        print(i, "es impar")
```

---

## 🔹 5. Buenas prácticas

* Usar buena indentación
* Evitar bucles infinitos
* Nombres de variables claros
* Simplificar condiciones

---

## 🚀 Ejemplo completo

```python
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
```
