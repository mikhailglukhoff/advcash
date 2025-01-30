# Этап 1: Сборка кода и страницы
FROM python:3.10 as builder

# Копируем все файлы и папки из текущей директории в контейнер
COPY . /app

WORKDIR /app

# Устанавливаем зависимости
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Этап 2: Запуск бота
FROM builder as bot

CMD ["python", "main.py"]
