FROM python:latest
WORKDIR ./Mailing
COPY . /Mailing
RUN pip install -r requirements.txt
RUN ["python", "manage.py", "makemigrations"]

EXPOSE 8000
