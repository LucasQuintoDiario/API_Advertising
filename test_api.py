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
