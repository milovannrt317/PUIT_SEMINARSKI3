FROM python:3.8

WORKDIR /pit

ADD . /pit
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

CMD ["python","manage.py","runserver"]
