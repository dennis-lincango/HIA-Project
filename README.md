# 📘 Trabajo académico final - Herramientas de la IA

Este repositorio contiene el análisis y visualización del mercado de productos electrónicos, desarrollado como parte del proyecto final para la materia de Inteligencia Artificial Aplicada.


## 👥 Autores

- **Lincango Simbaña Betsy Belén**
- **Lincango Simbaña Dennis David**


## 📊 Descripción del Proyecto

El proyecto incluye:
- Análisis exploratorio de datos (EDA) sobre productos electrónicos.
- Visualización interactiva de precios, marcas y comerciantes.
- Uso de herramientas como Python, Pandas, Matplotlib, Pygwalker y Streamlit.
- Generación de datos sintéticos para simulación de mercado.


## 🔗 Enlaces Relacionados

- 📖 Wiki del proyecto: [Análisis del mercado de productos electrónicos](https://github.com/dennis-lincango/HIA-Project/wiki)
- 📁 Repositorio: [HIA-Project](https://github.com/dennis-lincango/HIA-Project)
- 🌐 Página Web: [Trabajo académico final](https://dennis-lincango.github.io/HIA-Project/)


## 🚀 Instrucciones para instalación y ejecución

Sigue estos pasos para clonar y ejecutar el proyecto en tu máquina local:

### 1. Clonar el repositorio desde GitHub

Abre una terminal y ejecuta:

```bash
git clone https://github.com/dennis-lincango/HIA-Project.git
```

### 2. Crear y activar un entorno virtual (opcional, pero recomendado)

En Windows
```bash
python -m venv .venv
.venv\Scripts\activate
```

En Linux/macOS:
```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Instalar las dependencias

Instala las dependencias
```bash
pip install --upgrade pip
pip install -r requirements.txt
```

### 4. Crear la tabla y agregar datos en la base de datos de Azure (opcional)
Este paso es opcional si ya existe una tabla con datos ficticios. Para ejecutarlo:
```bash
python ../db/run.py
```


### 5. Ejecutar el análisis en Jupyter Notebook
Abre y ejecuta el siguiente notebook:
```bash
jupyter notebook ../notebooks/analytics.ipynb
```
