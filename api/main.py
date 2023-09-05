from fastapi import FastAPI
from pydantic import BaseModel, Field
from typing import List, Optional
import pickle
from pathlib import Path
import pandas as pd
import numpy as np
from src.schemas import  PricePredictionRequest, PricePrediction


app = FastAPI(
    title="Determining the cost of cars"
)

def get_model():
    """ Function to get model """
    with open('data/model.pkl', 'rb') as model_path:
        model = pickle.load(model_path)
    return model

model = get_model()
ohe = model['ohe']
model_lgbm = model['model']
scaler = model['scaler']


@app.post('/predict', response_model=List[float])
async def predict(request: PricePredictionRequest):
    data = [car.dict() for car in request.cars]
    df = pd.DataFrame(data)
    encoded_data = ohe.transform(df[ohe.feature_names_in_])
    X_new = np.concatenate((encoded_data, df[['RegistrationYear', 'Power', 'Kilometer']].values), axis=1)
    X_train = scaler.transform(X_new)
    pred = model_lgbm.predict(X_train)
    return pred
