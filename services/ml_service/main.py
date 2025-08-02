from fastapi import FastAPI
from .fast_api_handler import FastApiHandler
from prometheus_fastapi_instrumentator import Instrumentator
from prometheus_client import Histogram, Counter

app = FastAPI()
app.handler = FastApiHandler()

# инициализируем и запускаем экпортёр метрик
instrumentator = Instrumentator()
instrumentator.instrument(app).expose(app)

# Ручные метрики для дашборда ###
main_app_predictions = Histogram(
    'main_app_predictions',
    'Гистограмма цен',
    buckets=[1e6, 3e6, 5e6, 8e6, 1e7, 1.2e7, 1.5e7, 2e7, 3e7]
)

main_app_count = Counter('main_app_count', 'Счётчик запросов')


@app.get("/health")
def health_check():
    return {"status": "ok"}


@app.post('/api/predict/')
def get_prediction(model_params: dict):
    # Получаем предсказание от модели
    response = app.handler.handle(model_params)
    price = response.get('prediction', 0)

    # Обновляем метрики вручную
    main_app_predictions.observe(price)
    main_app_count.inc()

    return response
