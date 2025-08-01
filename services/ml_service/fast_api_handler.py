import os
import joblib
import numpy as np
import pandas as pd
# from catboost import CatBoostRegressor
from .variables import MODEL_PATH, REQUIRED_MODEL_PARAMS


class FastApiHandler:
    """Класс FastApiHandler, который обрабатывает запрос и возвращает предсказание."""

    def __init__(self):
        self.base_dir = os.path.dirname(os.path.abspath(__file__))
        self.model_path = os.path.join(self.base_dir, MODEL_PATH)
        self.pipeline = None  # инициализация
        self.model = None
        self.required_model_params = REQUIRED_MODEL_PARAMS
        self.feature_order = None
        self.load_model()

    def load_model(self):
        """Загружаем модель с метаданными"""
        try:
            # Проверка существования файла модели
            if not os.path.exists(self.model_path):
                raise FileNotFoundError(
                    f"Model file not found at {self.model_path}")

            # Загрузка модели
            self.pipeline = joblib.load(self.model_path)
            self.model = self.pipeline.named_steps['model']

            # Проверка метаданных (теперь у pipeline)
            if not hasattr(self.pipeline, 'feature_names'):
                raise ValueError(
                    "Pipeline is missing 'feature_names' attribute")

            self.feature_order = self.pipeline.feature_names
            print("Model loaded successfully")
            print(f"Feature names: {self.feature_order}")  # Для отладки

        except Exception as e:
            print(f"Model is not loaded: {e}")
            raise

    def validate_query_params(self, params: dict) -> bool:
        """Проверяем, что все необходимые параметры присутствуют"""
        if not isinstance(params, dict):
            return False
        return all(param in params for param in self.required_model_params)

    def predict(self, input_data: dict):
        """Делаем предсказание на основе входных данных"""
        # Валидация входных данных
        if not isinstance(input_data, dict):
            raise TypeError("Input data must be a dictionary")

        missing = set(self.feature_order) - set(input_data.keys())
        if missing:
            raise ValueError(f"Missing required features: {missing}")

        # Создаем DataFrame с правильным порядком признаков
        df = pd.DataFrame([input_data], columns=self.feature_order)

        # Предсказание
        log_prediction = self.pipeline.predict(df)[0]

        # Обратное преобразование таргета
        return float(np.expm1(log_prediction))

    def handle(self, params):
        try:
            if not self.validate_query_params(params):
                response = {
                    "Error": "Parameters do not correspond to expected."}
            else:
                if self.pipeline is None:
                    raise ValueError("Model is not loaded.")
                price_prediction = self.predict(params)
                response = {'predicted price': price_prediction}
        except Exception as e:
            response = {"Error": f"Problem with request: {e}"}

        return response


if __name__ == '__main__':
    # тестовый запрос
    data = {
        "build_year": 1970,
        "building_type_int": 6,
        "latitude": 55.87674331665039,
        "longitude": 37.570579528808594,
        "ceiling_height": 2.64,
        "flats_count": 84,
        "floors_total": 12,
        "has_elevator": true,
        "floor": 11,
        "kitchen_area": 11.0,
        "living_area": 46.0,
        "rooms": 3,
        "is_apartment": false,
        "total_area": 70.0
    }

    # обработчик запросов для API
    handler = FastApiHandler()

    # делаем тестовый запрос
    response = handler.handle(data)
    print(f"Response: {response}")
