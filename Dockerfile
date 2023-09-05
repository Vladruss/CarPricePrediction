
# RUN apt-get update && apt-get install -y libgomp1

# RUN mkdir /app

# COPY requirements.txt /app

# # Устанавливаем зависимости
# RUN pip3 install -r /app/requirements.txt --no-cache-dir

# # Копируем файл приложения в контейнер
# COPY api/ /app

# WORKDIR /app

# # Запускаем приложение при старте контейнера
# CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]


FROM python:3.10

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY api/ .

# RUN chmod a+x docker/*.sh

# WORKDIR api

CMD gunicorn main:app --workers 4 --worker-class uvicorn.workers.UvicornWorker --bind=0.0.0.0:8000 