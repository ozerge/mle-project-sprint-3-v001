import joblib
import numpy as np
from catboost import CatBoostRegressor
from variables import MODEL_PATH, REQUIRED_MODEL_PARAMS


class FastApiHandler:
    """Класс FastApiHandler, который обрабатывает запрос и возвращает предсказание."""

    def __init__(self):
        self.base_dir = os.path.dirname(os.path.abspath(__file__))
        self.model_path = os.path.join(self.base_dir, MODEL_PATH)
        self.pipeline_model = None  # инициализация
        self.required_model_params = REQUIRED_MODEL_PARAMS
        self.load_model()
