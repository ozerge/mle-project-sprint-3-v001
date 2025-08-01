import requests
import random
import time
import json  # Добавлен модуль для ручной проверки JSON

url = 'http://localhost:8081/api/predict/'


def generate_random_data():
    """Генерация случайных данных в формате ввода для предсказания, с правильными JSON-булевыми значениями"""
    return {
        "build_year": random.randint(1900, 2022),
        "building_type_int": random.randint(1, 10),
        "latitude": round(random.uniform(55.0, 56.0), 6),
        "longitude": round(random.uniform(37.0, 38.0), 6),
        "ceiling_height": round(random.uniform(2.0, 3.5), 2),
        "flats_count": random.randint(1, 100),
        "floors_total": random.randint(1, 30),
        "has_elevator": random.choice([False, True]),
        "floor": random.randint(1, 30),
        "kitchen_area": round(random.uniform(5, 20), 2),
        "living_area": round(random.uniform(10, 50), 2),
        "rooms": random.randint(1, 5),
        "is_apartment": random.choice([False, True]),
        "total_area": round(random.uniform(20, 100), 2)
    }


def simulate_load(number_of_requests, delay_between_requests=0):
    for i in range(number_of_requests):
        data = generate_random_data()

        # Для отладки: проверка преобразования в JSON
        json_data = json.dumps(data)
        # Убедимся, что булевы значения верные
        print(f"Generated JSON: {json_data}")

        try:
            response = requests.post(
                url,
                json=data,  # requests автоматически конвертирует в правильный JSON
                headers={'Content-Type': 'application/json'}
            )

            print(f"\nRequest {i+1}/{number_of_requests}:")
            print(f"Status: {response.status_code}")
            print(f"Response: {response.text}\n")

        except Exception as e:
            print(f"Error: {str(e)}")

        if delay_between_requests > 0:
            time.sleep(delay_between_requests)


if __name__ == '__main__':
    simulate_load(100, 1)
