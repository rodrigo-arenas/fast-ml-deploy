import models.ml.classifier as clf
from fastapi import FastAPI, Body
from joblib import load
from models.iris import Iris

app = FastAPI(title="Medium ML API", description="API for iris dataset ml model", version="1.0")


@app.on_event('startup')
def load_model():
    clf.model = load('models/ml/iris_rf_v1.joblib')


@app.post('/predict', tags=["predictions"])
async def get_prediction(iris: Iris):
    data = dict(iris)['data']
    prediction = clf.model.predict(data).tolist()
    log_proba = clf.model.predict_proba(data).tolist()
    print(log_proba)
    return {"prediction": prediction,
           "log_proba": log_proba}




