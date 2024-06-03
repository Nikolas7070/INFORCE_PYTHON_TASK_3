# Используйте базовый образ Python
FROM python:3.9-slim

# Установите системные зависимости
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Установите рабочую директорию
WORKDIR /app

# Скопируйте файлы с зависимостями в контейнер
COPY requirements.txt .

# Обновите pip до последней версии
RUN pip install --upgrade pip

# Установите Python-зависимости и выведите информацию для диагностики
RUN pip install --no-cache-dir -r requirements.txt

# Скопируйте остальные файлы приложения в контейнер
COPY . .

# Определите команду запуска контейнера
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
