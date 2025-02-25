# FastAPI Sales Prediction API

Este repositorio contiene una API creada con **FastAPI** para predecir ventas en función de datos de inversión en publicidad. Se incluyen funcionalidades para realizar predicciones, consultar datos almacenados y reentrenar el modelo.

## 🚀 Instalación y Uso

### 1️⃣ Clonar el Repositorio
```bash
git clone https://github.com/LucasQuintoDiario/API_Advertising.git
cd API_Advertising
```

### 2️⃣ Configurar y Construir la Imagen con Docker
Si deseas ejecutar la API con Docker, simplemente usa:
```bash
docker-compose up --build
```
Esto descargará las dependencias y ejecutará la API en **http://localhost:8000**.

### 3️⃣ Uso de la API con Postman
Puedes interactuar con la API utilizando **Postman** siguiendo estos pasos:

1. Abre **Postman** y crea una nueva petición.
2. Configura la **URL base** de la API: `http://localhost:8000`.
3. Usa los siguientes detalles para cada endpoint:

#### 🔹 Predecir ventas
- **Método:** `POST`
- **URL:** `http://localhost:8000/predict`
- **Body (JSON):**
  ```json
  {
    "TV": 100.0,
    "radio": 20.0,
    "newspaper": 10.0
  }
  ```
- **Configura el header:**
  - `Content-Type: application/json`

#### 🔹 Consultar datos almacenados
- **Método:** `GET`
- **URL:** `http://localhost:8000/consult`

#### 🔹 Ingresar nuevos datos
- **Método:** `POST`
- **URL:** `http://localhost:8000/ingest`
- **Body (JSON):**
  ```json
  {
    "TV": 150.0,
    "radio": 30.0,
    "newspaper": 20.0,
    "sales": 25.5
  }
  ```
- **Headers:**
  - `Content-Type: application/json`

#### 🔹 Reentrenar el modelo
- **Método:** `GET`
- **URL:** `http://localhost:8000/retrain`


## 🧪 Testeo de la API
Para probar los endpoints de la API, puedes ejecutar los tests desde una terminal, navegar al directorio donde se encuentra el archivo test_api.py. Luego ejecuta el siguiente comando:

```bash
pytest test_api.py

```

## 📜 Licencia
Este proyecto está bajo la licencia **MIT**. ¡Siéntete libre de contribuir y mejorar! 🚀