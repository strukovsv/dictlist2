FROM python:3.11

ENV PYTHONPATH="/app"
ENV PYTHONUNBUFFERED=1 PYTHONDONTWRITEBYTECODE=1

# Перейти в рабочий директорий
WORKDIR /tests
WORKDIR /app

# Установить зависимости
COPY requirements.txt ./
RUN python -m pip install --no-cache-dir --upgrade pip \
  && pip install --verbose --no-cache-dir -r requirements.txt

# Скопировать выполняемый код
COPY ./src/. ./

CMD ["python", "-m", "main"]

