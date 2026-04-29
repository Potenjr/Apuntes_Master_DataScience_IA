# 📘 FUNDAMENTOS DE PROGRAMACIÓN Y PYTHON

## 🧠 CLASE 1

---

## 🔄 Fases de un Proyecto

Un proyecto completo sigue estos 6 pasos:

1. **Problema**

   * Definir qué se quiere resolver

2. **Datos**

   * Obtener datos (CSV, APIs, bases de datos, etc.)

3. **EDA (Análisis Exploratorio de Datos)**

   * Limpieza de datos
   * Análisis
   * Visualización

4. **Modelado**

   * Aplicación de modelos o algoritmos

5. **Producto**

   * Desarrollo de una aplicación (ej: Streamlit)

6. **Comunicación**

   * Presentación de resultados
   * Visualizaciones e informe

---

## ⚙️ Entornos Virtuales en Windows

Los entornos virtuales permiten aislar las dependencias de cada proyecto.

### 📦 Crear entorno virtual

```bash
python -m venv venv
```

---

### 🔐 Solución a error en PowerShell

Si aparece error al activar el entorno:

```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

---

### ▶️ Activar entorno

```bash
venv\Scripts\activate
```

---

### ⛔ Desactivar entorno

```bash
venv\Scripts\deactivate
```

---

### 📄 Guardar dependencias

Crear archivo `requirements.txt` con todas las librerías:

```bash
pip freeze > requirements.txt
```

---

## 💡 Notas importantes

* Usar un entorno virtual por cada proyecto
* Nombrar el entorno como `venv` (convención estándar)
* El archivo `requirements.txt` permite replicar el entorno

---

## 🚀 Flujo de trabajo recomendado

1. Crear entorno virtual
2. Activarlo
3. Instalar librerías (`pip install ...`)
4. Guardar dependencias
5. Desarrollar el proyecto

---
