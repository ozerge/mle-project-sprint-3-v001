import os
import joblib
from catboost import CatBoostClassifier
from variables import MODEL_PATH


def load_churn_model(model_path: str):
    """Загружаем обученную модель.
    Args:
        model_path (str): Путь до модели.
    """
    try:
        # Проверяем существование файла
        if not os.path.exists(model_path):
            raise FileNotFoundError(f"Model file not found at {model_path}")

        # Загружаем модель в зависимости от расширения файла
        if model_path.endswith('.pkl'):
            model = joblib.load(model_path)
        else:
            model = CatBoostClassifier()
            model.load_model(model_path)

        print("Model loaded successfully")
        return model
    except Exception as e:
        print(f"Failed to load model: {e}")
        return None


if __name__ == "__main__":
    # Получаем абсолютный путь к модели
    current_dir = os.path.dirname(os.path.abspath(__file__))
    model_path = os.path.join(current_dir, MODEL_PATH)

    # Загружаем модель
    model = load_churn_model(model_path)

    # Выводим параметры модели
    if model is not None:
        print(
            f"Model parameter names: {model.feature_names if hasattr(model, 'feature_names') else 'Not available'}")
    else:
        print("Model is not loaded")
