# This Dockerfile WORKS but is full of bad habits. Your job (exercise 3) is to fix it.
FROM python
ADD . /app
WORKDIR /app
RUN pip install flask
RUN pip install gunicorn
RUN apt-get update
RUN apt-get install -y curl
CMD python app/app.py
