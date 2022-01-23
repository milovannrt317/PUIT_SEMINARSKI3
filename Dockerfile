FROM python:3.8

WORKDIR /pit

ADD . /pit
RUN chmod 777 /pit
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

CMD ["python","manage.py","runserver","0.0.0.0:8000"]
