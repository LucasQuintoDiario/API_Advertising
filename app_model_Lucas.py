from fastapi import FastAPI
from pydantic import BaseModel
import numpy as np
import sqlite3
import uvicorn
import pickle
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import StandardScaler, PolynomialFeatures

with open("data/advertising_model.pkl", "rb") as f:
    model = pickle.load(f)


app = FastAPI()

class Features(BaseModel):
    TV: float
    radio: float
    newspaper: float

class TrainingData(BaseModel):
    TV: float
    radio: float
    newspaper: float
    sales: float

@app.get("/")
async def hello():
    return {"message": "Calcula ventas con datos de otras cosas, Salu2"}

@app.get("/consult/")
async def  consulta():
    conn = sqlite3.connect('data/prediccion_ventas.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Advertising")
    rows = cursor.fetchall()
    conn.close()
    columns = [description[0] for description in cursor.description]
    result = [dict(zip(columns, row)) for row in rows]
    return {"data": result}


@app.post("/predict/")
async def predict(features: Features):
    data_predict = np.array([[features.TV, features.radio, features.newspaper]])
    prediction = model.predict(data_predict)
    return {"predicted_sales": float(prediction[0])}

@app.post("/ingest/")
async def predict(features: TrainingData):
    conn = sqlite3.connect('data/prediccion_ventas.db')
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO Advertising (TV, Radio, Newspaper, Sales)
        VALUES (?, ?, ?, ?)
    ''', (features.TV, features.radio, features.newspaper, features.sales))
    conn.commit()
    conn.close()

    return {"message": "Datos subidos correctamente"}


@app.get("/retrain/")
async def retrain():
    conn = sqlite3.connect('data/prediccion_ventas.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Advertising")
    rows = cursor.fetchall()
    conn.close()
    X = np.array([[row[0], row[1], row[2]] for row in rows])
    y = np.array([row[3] for row in rows])
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)
    pol_3 = PolynomialFeatures(degree = 3)
    pol_3.fit_transform(X_scaled)
    model = LinearRegression()
    model.fit(X_scaled, y)
    with open("data/advertising_model.pkl", "wb") as f:
        pickle.dump(model, f)
    return {"message": "Modelo reentrenado y guardado correctamente"}


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)