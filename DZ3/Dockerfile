FROM python:3.9
RUN mkdir /app
COPY ./django/ /app
WORKDIR /app
RUN pip3 install -r requirements.txt
WORKDIR /app/app
ENTRYPOINT ["python3","manage.py","runserver","0.0.0.0:8765"]
EXPOSE 8765
