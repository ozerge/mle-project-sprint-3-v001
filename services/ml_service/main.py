from fastapi import FastAPI, Body
from fast_api_handler import FlatPriceHandler

app = FastAPI()

app.handler = FlatPriceHandler()


@app.post('/api/predict/')
def get_prediction(model_params: dict):
    return app.handler.handle(model_params)
