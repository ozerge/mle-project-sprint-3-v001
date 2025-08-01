# Инструкции по запуску микросервиса

Каждая инструкция выполняется из директории репозитория mle-sprint3-completed
Если необходимо перейти в поддиректорию, напишите соотвесвтующую команду

## 1. FastAPI микросервис в виртуальном окружение
```python
# Установка расширения для виртуального пространства:
sudo apt-get install python3.10-venv
```
```bash
# Создание виртуального пространства:
python3.10 -m venv .mle-sprint3-venv
```
```bash
# Активируйте виртуальное пространство:
source .mle-sprint3-venv/bin/activate
```
```bash
# Установка необходимых библиотек:
pip install -r requirements.txt
```
```bash
# Команда перехода в директорию:
cd ./services/
```
```bash
# Команда запуска сервиса с помощью uvicorn:
uvicorn ml_service.main:app --reload --port 8081 --host 0.0.0.0
```
```bash
# Для просмотра документации API и совершения тестовых запросов зайти на [http://localhost::8081/docs](http://localhost::8081/docs)<br>.
# команда остановки микросервиса в терминале - нажатие клавиш Ctrl+C
```
### Пример curl-запроса к микросервису

```bash
curl -X 'POST' \
  'http://localhost:8081/api/predict/' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
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
    }'
```


## 2. FastAPI микросервис в Docker-контейнере

```bash
# Команда перехода в нужную директорию:
cd ./services/
```
```bash
# Собираем образ:
docker build -f Dockerfile_ml_service . --tag price_predict:0
```
```bash
# Загрузите переменные из .env:
export $(grep -v '^#' .env | xargs)
```
```bash
# Команда для запуска микросервиса в режиме docker:
docker container run --publish ${APP_PORT}:${APP_PORT} --volume=./models:/real_estate/models   --env-file .env price_predict:0
```
```bash
# в фоновом режиме:
docker container run -d --publish ${APP_PORT}:${APP_PORT} --volume=./models:/real_estate/models   --env-file .env price_predict:0
```
```bash
# Для просмотра документации API и совершения тестовых запросов зайти на [http://localhost::8081/docs](http://localhost::8081/docs)<br>.
```
```bash
# Проверка статуса контейнера:
docker container ls -a | grep price_predict:0
```
```bash
# или запущенные контейнеры:
docker ps
```
```bash
# Остановка контейнера:
docker stop <ID контейнера>
```
```bash
# Удаление контейнера:
docker rm <ID контейнера>
```

### Пример curl-запроса к микросервису

```bash
curl -X 'POST' \
  'http://localhost:8081/api/predict/' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
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
    }'
```

## 3. Docker compose для микросервиса и системы моониторинга

```bash
# команда перехода в нужную директорию
cd ./services/
```
```bash
# Загрузите переменные из .env:
export $(grep -v '^#' .env | xargs)
```
```bash
# команда для запуска микросервиса в режиме docker compose
docker compose up --build
```
```bash
# в фоновом режиме:
docker compose up --build -d
```
```bash
# Для просмотра документации API и совершения тестовых запросов зайти на [http://localhost::8081/docs](http://localhost::8081/docs)<br>.
# команда остановки микросервиса в терминале - нажатие клавиш Ctrl+C
# остановка работающего в фоновом режиме:
docker compose down
```

### Пример curl-запроса к микросервису

```bash
curl -X 'POST' \
  'http://localhost:8081/api/predict/' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
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
    }'
```

## 4. Скрипт симуляции нагрузки
Скрипт генерирует <...> запросов в течение <...> секунд ...

```
# команды необходимые для запуска скрипта
...
```

Адреса сервисов:
- микросервис: http://localhost:<port>
- Prometheus: ...
- Grafana: ...