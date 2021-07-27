"""The main module."""

from fastapi import FastAPI
from dummy.dummy_app import process_data
from pydantic import BaseModel


class Item(BaseModel):
    symbols: list[str]


app = FastAPI()


@app.get('/')
async def root() -> dict:
    """Root AP."""
    return {'msg': 'Welcome!'}


@app.post('/predict')
async def predict(request: Item) -> dict:
    """Root AP."""
    processed_data = process_data(request.symbols)
    return {'processed_data': processed_data}
