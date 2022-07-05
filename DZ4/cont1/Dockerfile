FROM python:rc-alpine

RUN mkdir /app
COPY . /app

WORKDIR /app
RUN pip install -r requirements.txt

EXPOSE 5000

ENV FLASK_APP=main.py
ENV FLASK_DEBUG=1

CMD ["flask", "run", "--host", "0.0.0.0"]
