import models.ml.classifier as clf
import numpy as np
from fastapi import FastAPI
from joblib import load
from models.iris import Iris, IrisPredictionResponse

app = FastAPI(title="Iris ML API", description="API for iris dataset ml model", version="1.0")


@app.on_event('startup')
async def load_model():
    clf.model = load('models/ml/iris_dt_v1.joblib')
    np.seterr(divide='warn')


@app.get('/', tags=["Intro"])
async def hello():
    return {"message": "Hello!"}


@app.post('/predict', tags=["predictions"],
          response_model=IrisPredictionResponse)
async def get_prediction(iris: Iris):
    data = dict(iris)['data']
    prediction = clf.model.predict(data).tolist()
    log_probability = clf.model.predict_log_proba(data).tolist()
    return {"prediction": prediction,
            "log_probability": log_probability}
