FROM python:3.6.1-alpine

RUN pip install --upgrade pip
RUN pip install Flask pymongo dnspython colorama 

WORKDIR /app

COPY . /app
EXPOSE 5000
CMD 'python3' 'app.py'