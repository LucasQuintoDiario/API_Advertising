from fastapi import FastAPI
from fastapi.responses import HTMLResponse
import numpy as np
import sqlite3
import uvicorn
import pickle
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import StandardScaler, PolynomialFeatures

with open("data/advertising_model.pkl", "rb") as f:
    model = pickle.load(f)


app = FastAPI()


@app.get("/", response_class=HTMLResponse)
async def hello():
    return """
    <html>
        <head>
            <title>API de Predicción de Ventas</title>
            <style>
                body { font-family: Arial, sans-serif; margin: 40px; text-align: center; }
                h1 { color: #007BFF; }
                p { font-size: 18px; color: #333; }
                .container { max-width: 600px; margin: auto; padding: 20px; border-radius: 10px; 
                             box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.2); background-color: #f9f9f9; }
            </style>
        </head>
        <body>
            <div class="container">
                <h1>API de Predicción de Ventas</h1>
                <p>🚀 Calcula las ventas en base a la inversión en:</p>
                <ul>
                    <li><b>📺 TV</b></li>
                    <li><b>📻 Radio</b></li>
                    <li><b>📰 Periódicos</b></li>
                </ul>
                <p>📊 Consulta los datos almacenados en la base de datos.</p>
                <p>📝 Introduce nuevos datos.</p>
                <p>🔄 Reentrena el modelo con los datos añadidos.</p>
                <p><b>💡 Usa la documentación interactiva en <a href='/docs' target='_blank'>/docs</a></b></p>
            </div>
        </body>
    </html>
    """


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
async def predict(data:dict):
    try:
        data_predict = data.get('data')
        prediction = model.predict(data_predict).tolist()
        return {"prediction": prediction}
    except Exception as e:
        return {"error": str(e)}



@app.post("/ingest/")
async def ingest(data:dict):
    data_ingest = data.get("data")
    conn = sqlite3.connect('data/prediccion_ventas.db')
    cursor = conn.cursor()
    cursor.executemany('''
        INSERT INTO Advertising (TV, Radio, Newspaper, Sales)
        VALUES (?, ?, ?, ?)
    ''', (data_ingest))
    conn.commit()
    conn.close()

    return {'message': 'Datos ingresados correctamente'}

@app.post("/retrain/")
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
    return {'message': 'Modelo reentrenado correctamente.'}


if __name__ == "__main__":
    uvicorn.run(app)