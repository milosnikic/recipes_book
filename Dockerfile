FROM python:3.10


ENV PYTHONUNBUFFERED 1

RUN mkdir src

COPY . /src/

WORKDIR /src

RUN pip install -r requirements.txt

WORKDIR /src/backend

EXPOSE 8000

VOLUME /src

CMD python manage.py makemigrations && python manage.py migrate && python manage.py runserver 0.0.0.0:8000