# Берем официальный легкий образ Python
FROM python:3.11-slim

# Устанавливаем системные зависимости для работы с Postgres
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Устанавливаем рабочую папку внутри контейнера
WORKDIR /app

# Запрещаем Python писать файлы .pyc на диск и буферизовать вывод (для красивых логов)
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Копируем и устанавливаем зависимости
COPY requirements.txt /app/
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Копируем весь проект в контейнер
COPY . /app/
