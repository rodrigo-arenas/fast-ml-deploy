from fastapi import APIRouter
from models.schemas.iris import Iris, IrisPredictionResponse
import models.ml.classifier as clf

app_iris_predict_v1 = APIRouter()


@app_iris_predict_v1.post('/iris/predict',
                          tags=["Predictions"],
                          response_model=IrisPredictionResponse,
                          description="Get a classification from Iris")
async def get_prediction(iris: Iris):
    data = dict(iris)['data']
    prediction = clf.model.predict(data).tolist()
    probability = clf.model.predict_proba(data).tolist()
    log_probability = clf.model.predict_log_proba(data).tolist()
    return {"prediction": prediction,
            "probability": probability,
            "log_probability": log_probability}

