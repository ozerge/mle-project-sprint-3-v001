from fastapi import FastAPI
from .fast_api_handler import FastApiHandler

app = FastAPI()
app.handler = FastApiHandler()


@app.get("/health")
def health_check():
    return {"status": "ok"}


@app.post('/api/predict/')
def get_prediction(model_params: dict):
    return app.handler.handle(model_params)
