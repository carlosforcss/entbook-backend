FROM python:3.7
ENV PYTHONUNBUFFERED 1
ENV DJANGO_SETTINGS_MODULE=config.settings.production

RUN mkdir /app
WORKDIR /app
COPY requirements.txt /app/

RUN pip install -r requirements.txt
COPY . /app/
CMD gunicorn config.wsgi:application --bind 0.0.0.0:8000
