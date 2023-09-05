from pydantic import BaseModel, Field
from typing import List


class PricePrediction(BaseModel):
    VehicleType: str = 'uknown'
    RegistrationYear: int = Field(ge=1900)
    Gearbox: str = 'uknown'
    Power: int = Field(ge=0)
    Model: str = 'uknown'
    Kilometer: int = Field(ge=0)
    FuelType: str = 'uknown'
    Brand: str = 'uknown'
    Repaired: str = 'uknown'


class PricePredictionRequest(BaseModel):
    cars: List[PricePrediction] 
