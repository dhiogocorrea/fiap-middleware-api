from fastapi import FastAPI
from pydantic import BaseModel
from service import message
from fastapi.encoders import jsonable_encoder


class Data(BaseModel):
    selectedSymptoms: str = Field(None)
    yearOfBirth: str = Field(None)
    gender: str = Field(None)


app = FastAPI(
    title="Middeware for DoctorBOT",
    description="",
    version="1.0.0")

@app.post("/")
def get_message(data: Data):
    return jsonable_encoder(message(data))