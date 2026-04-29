# 💻 COMANDOS PARA WINDOWS (POWERSHELL)

👉 Usa esta chuleta solo si no has podido instalar **Git Bash**.
La clase está pensada para **Mac / Linux / Git Bash**, por lo que en PowerShell algunos comandos cambian.

---

## 🐍 ENTORNOS VIRTUALES Y PYTHON (WINDOWS)

* `python -m venv venv` → Crea un entorno virtual llamado `venv`
* `.\venv\Scripts\Activate.ps1` → Activa el entorno virtual
* `deactivate` → Desactiva el entorno virtual
* `pip install -r requirements.txt` → Instala dependencias
* `pip freeze > requirements.txt` → Guarda dependencias

---

## 📁 COMANDOS BÁSICOS DE TERMINAL (POWERSHELL)

* `pwd` → Muestra la ruta actual
* `cd ~` → Ir al directorio personal
* `cd ..` → Subir un nivel
* `ls` → Listar archivos y carpetas
* `Get-ChildItem -Force` → Mostrar archivos ocultos

---

### 📂 Gestión de carpetas y archivos

* `mkdir nombrecarpeta` → Crear carpeta
* `mkdir nom1, nom2, nom3` → Crear varias carpetas
* `New-Item archivo.txt -ItemType File` → Crear archivo vacío

---

### 📄 Manipulación de archivos

* `Copy-Item notas.txt backup_notas.txt` → Copiar archivo
* `Move-Item backup_notas.txt output/` → Mover archivo
* `Remove-Item archivo.txt` → Eliminar archivo
* `Remove-Item carpeta -Recurse -Force` → Eliminar carpeta

---

### ✏️ Escribir y leer archivos

* `Set-Content archivo.txt "Hola terminal"` → Escribir contenido
* `Add-Content saludo.txt "Texto"` → Añadir contenido
* `Get-Content archivo.txt` → Leer archivo
* `Get-Content archivo.txt | more` → Leer paginado

---

### 🌳 Estructura de carpetas

* `tree` → Ver estructura
* `tree /F` → Ver con archivos
* `tree /A` → Formato ASCII

---

## 🔍 BUSCAR ARCHIVOS Y TEXTO

* `Get-ChildItem -Recurse -Filter *.txt` → Buscar archivos `.txt`
* `Get-ChildItem -Recurse -Filter archivo.txt` → Buscar por nombre
* `Get-ChildItem -Recurse -File | Select-String "texto"` → Buscar dentro de archivos

---

## ▶️ EJECUTAR PYTHON EN WINDOWS

* `python .\archivo.py` → Ejecutar script
* `py .\archivo.py` → Alternativa
* `python .\script.py argumento` → Ejecutar con parámetros

---

## ⚠️ NOTA IMPORTANTE

En clase se usarán comandos de **Mac**.

* En **Git Bash** → funcionan casi igual
* En **PowerShell** → usa esta guía como referencia

---

# 🛠️ CONFIGURACIÓN DE LA TERMINAL

## 🍎 Usuarios de Mac / Linux

✅ No necesitas instalar nada

Prueba:

```bash
pwd
ls
```

---

## 🪟 Usuarios de Windows (RECOMENDADO)

👉 Usa **Git Bash** para evitar problemas de compatibilidad.

---

### 📥 Paso 1: Instalación

1. Ir a: https://git-scm.com/download/win
2. Descargar instalador
3. Ejecutarlo
4. Pulsar **Next** en todo (configuración por defecto)

---

### 🔗 Paso 2: Conectar con VS Code

1. Abrir VS Code
2. `Ctrl + Shift + P`
3. Buscar: `Terminal: Select Default Profile`
4. Elegir **Git Bash**
5. Abrir nueva terminal (`Ctrl + ñ`)

👉 Si ves `$` → todo correcto

---

## 🚑 PLAN B: PowerShell

Si no puedes instalar Git Bash:

* Usa PowerShell
* Ten en cuenta que algunos comandos cambian

---

## 🔄 Equivalencias básicas

| Acción           | Mac / Git Bash       | PowerShell                            |
| ---------------- | -------------------- | ------------------------------------- |
| Ver ruta         | `pwd`                | `pwd`                                 |
| Listar archivos  | `ls`                 | `ls`                                  |
| Navegar carpetas | `cd`                 | `cd`                                  |
| Ver ocultos      | `ls -a`              | `Get-ChildItem -Force`                |
| Crear archivo    | `touch archivo.txt`  | `New-Item archivo.txt -ItemType File` |
| Ejecutar Python  | `python3 archivo.py` | `python archivo.py`                   |

---

## 💡 Recomendación final

👉 Si puedes elegir: **usa Git Bash**
👉 Si no: PowerShell + esta chuleta

---
# 🖥️ Introducción a la Terminal (para Data Science)

Esta clase no va de memorizar comandos.
Va de **entender qué está pasando** cuando usas la terminal.

Piensa en la terminal como una conversación directa con tu ordenador:

* No hay botones
* No hay menús
* Solo instrucciones claras

> Si entiendes esto, el resto es vocabulario.

---

## ⚡ 0. Preparación rápida (2–3 min)

Abre una terminal:

* 🪟 Windows → **Git Bash** (recomendado) o PowerShell
* 🍎 Mac/Linux → Terminal

👉 Se enseñará en Mac, pero en Git Bash es igual
👉 Regla: prueba → observa → corrige

---

## 📁 1. Conceptos básicos

### Carpetas (directorios)

* Contenedores
* Pueden tener archivos y otras carpetas

### Archivos

* `.csv`, `.py`, `.txt`, etc.

👉 La terminal **siempre está en una carpeta concreta**

---

### ✅ Ejercicio 1

```bash id="ev9c32"
pwd
```

👉 Muestra la ruta actual

---

## 📍 2. ¿Dónde estoy?

### `pwd` → Print Working Directory

```bash id="4bc4xb"
pwd
```

Ejemplo:

```
/Users/alumno/Documentos
```

---

### ✅ Ejercicio 2

```bash id="flr5q9"
cd ~
pwd
```

👉 Esto es tu **home**

---

## 📂 3. ¿Qué hay aquí?

### `ls`

```bash id="z4r2y9"
ls
```

Variantes:

```bash id="rnx4qz"
ls -l
ls -a
```

---

### ✅ Ejercicio 3

```bash id="n1wz1k"
ls
ls -a
```

👉 Busca archivos que empiecen por `.`

---

## 🔄 4. Navegación

```bash id="2md6h1"
cd carpeta
cd ..
cd ~
cd -
```

💡 Usa `TAB` para autocompletar

---

### ✅ Ejercicio 4

```bash id="0c3l1n"
cd ~
ls
cd carpeta
pwd
cd ..
cd -
```

---

## 🏗️ 5. Crear archivos y carpetas

```bash id="pz5czh"
mkdir datos
touch notas.txt
```

---

### ✅ Ejercicio 5

```bash id="q6ojr3"
mkdir terminal_practica
cd terminal_practica
mkdir data scripts output
touch README.txt
ls
```

---

## 📦 6. Copiar y mover

```bash id="o8bbm1"
cp origen destino
mv origen destino
```

---

### ✅ Ejercicio 6

```bash id="q9s83p"
touch notas.txt
cp notas.txt backup_notas.txt
mv backup_notas.txt output/
ls output
```

---

## 📖 7. Leer archivos

```bash id="l5j9g3"
cat archivo.txt
less archivo.txt
```

---

### ✅ Ejercicio 7

```bash id="1fhg7x"
echo "Hola terminal" > saludo.txt
cat saludo.txt

echo "Estoy aprendiendo" >> saludo.txt
less saludo.txt
```

👉 `q` para salir

---

## 🗑️ 8. Borrar

```bash id="sdxqv2"
rm archivo.txt
rm -rf carpeta
```

⚠️ No va a la papelera

---

### ✅ Ejercicio 8

```bash id="87db5y"
touch borrar_esto.tmp
ls
rm borrar_esto.tmp
ls
```

---

## 🔍 9. Buscar archivos

```bash id="qpk8z2"
find . -name "*.txt"
find . -name "archivo.txt"
```

---

### ✅ Ejercicio 9

```bash id="xtg41k"
find . -name "*.txt"
find . -name "saludo.txt"
```

👉 `.` = desde aquí

---

## ▶️ 10. Ejecutar Python

```bash id="db7rx1"
python3 script.py
python script.py
```

---

### ✅ Ejercicio 10

```bash id="rl3jsh"
cd scripts
echo "print('Hola desde Python')" > hola.py
python3 hola.py
```

---

## 🧩 11. Laberinto (juego)

Objetivo:

* Encontrar la llave
* Descubrir el código
* Abrir el tesoro

---

### ▶️ Ejecutar

```bash id="o8yqq2"
python3 setup_juego.py
```

---

### 📋 Pasos

1. Entrar en carpeta
2. Leer `leeme.txt`
3. Seguir pistas
4. Encontrar `llave_sotano.txt`
5. Descubrir `CODIGO_COFRE`
6. Ejecutar comando final

---

### ✅ Checklist

* [ ] Entrar en carpeta
* [ ] Leer pistas
* [ ] Encontrar llave
* [ ] Encontrar código
* [ ] Ejecutar script final

---

### 💡 Pistas

```bash id="dnh3wr"
find . -name "PISTA_*.txt"
find . -name "llave_sotano.txt"
grep -R "CODIGO_COFRE" .
```

---

## 🧠 12. Lo aprendido

* Navegar archivos
* Usar terminal sin interfaz
* Buscar información
* Ejecutar scripts

> La terminal no es magia: es precisión.
