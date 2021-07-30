"""The main module."""

from fastapi import FastAPI
from stock_scrapper import version
from stock_scrapper.dummy.dummy_app import process_data
from stock_scrapper.webcrawl.get_prices import get_stocks_value
from pydantic import BaseModel


class Item(BaseModel):
    """Base schema."""

    symbols: list[str]

    class Config:
        """Usage example."""

        schema_extra = {
            'example': {
                'symbols': ['VVAR3', 'GOOGL34', 'AMER3']
            }
        }


app = FastAPI()


@app.get('/')
async def root() -> dict:
    """Root Endpoint."""
    return {'msg': f'Stock Scrapper API - updated on {version.version}!'}


@app.post('/predict_dummy')
async def predict_dummy(request: Item) -> dict:
    """Prediction Endpoint - dummy."""
    processed_data = process_data(request.symbols)
    return {'processed_data': processed_data}


@app.post('/predict')
async def predict(request: Item) -> dict:
    """Prediction Endpoint - real deal."""
    processed_data = get_stocks_value(request.symbols)
    return {'processed_data': processed_data}
