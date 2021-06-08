FROM python:3.8-slim-buster

EXPOSE 3306

ENV PYTHONDONTWRITTERBYTHECODE=1

ENV PYTHONUNBUFFERED=1

COPY requirements.txt .
RUN python -m pip install -r requirements.txt

WORKDIR /Ollivanders_api_rest
copy . /Ollivanders_api_rest

COPY requirements.txt requirements.txt

RUN pip3 install -r requirements.txt

COPY . .

CMD [ "python3", "api.py", "localhost:3306"]
