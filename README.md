# FastAPI Sales Prediction API

Este repositorio contiene una API creada con **FastAPI** para predecir ventas en función de datos de inversión en publicidad. Se incluyen funcionalidades para realizar predicciones, consultar datos almacenados y reentrenar el modelo.

## 🚀 Instalación y Uso

### 1️⃣ Clonar el Repositorio
```bash
git clone https://github.com/tu-usuario/tu-repositorio.git
cd tu-repositorio
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
- **URL:** `http://localhost:8000/predict/`
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
- **URL:** `http://localhost:8000/consult/`

#### 🔹 Ingresar nuevos datos
- **Método:** `POST`
- **URL:** `http://localhost:8000/ingest/`
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
- **URL:** `http://localhost:8000/retrain/`

## 🐳 Subir la Imagen a Docker Hub
Si quieres compartir la imagen en **Docker Hub**, sigue estos pasos:
```bash
docker login
docker tag fastapi_app tu-usuario/fastapi_app:latest
docker push tu-usuario/fastapi_app:latest
```
Luego, en otra máquina, puedes ejecutar:
```bash
docker pull tu-usuario/fastapi_app:latest
docker run -p 8000:8000 tu-usuario/fastapi_app
```

## 🧪 Testeo de la API
Para probar los endpoints de la API, puedes utilizar el siguiente código en Python:

```python
import requests

def test_ingest_endpoint():
    url = 'http://127.0.0.1:8000/ingest'  
    data = {'TV': 100.0, 'radio': 100.0, 'newspaper': 200.0, 'sales': 3000.0}
    response = requests.post(url, json=data)
    assert response.status_code == 200
    assert response.json() == {'message': 'Datos ingresados correctamente'}

def test_predict_endpoint():
    url = 'http://127.0.0.1:8000/predict'  
    data = {'TV': 100.0, 'radio': 100.0, 'newspaper': 200.0}
    response = requests.post(url, json=data)
    assert response.status_code == 200
    assert 'prediction' in response.json()

def test_retrain_endpoint():
    url = 'http://127.0.0.1:8000/retrain'  
    response = requests.get(url)
    assert response.status_code == 200
    assert response.json() == {'message': 'Modelo reentrenado correctamente.'}
```

Ejecuta este código en un entorno Python para verificar el correcto funcionamiento de la API.

## 📜 Licencia
Este proyecto está bajo la licencia **MIT**. ¡Siéntete libre de contribuir y mejorar! 🚀