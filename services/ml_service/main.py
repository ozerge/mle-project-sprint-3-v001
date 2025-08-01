from fastapi import FastAPI
from .fast_api_handler import FastApiHandler
from prometheus_fastapi_instrumentator import Instrumentator

app = FastAPI()
app.handler = FastApiHandler()

# инициализируем и запускаем экпортёр метрик
instrumentator = Instrumentator()
instrumentator.instrument(app).expose(app)


@app.get("/health")
def health_check():
    return {"status": "ok"}


@app.post('/api/predict/')
def get_prediction(model_params: dict):
    return app.handler.handle(model_params)
