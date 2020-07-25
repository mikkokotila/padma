FROM python:3.7.3
WORKDIR /project
ADD . /project
RUN apt-get update -y
RUN apt-get install -y enchant
RUN pip install --upgrade pip
RUN pip install cython
RUN pip install -r requirements.txt
RUN python3 -m spacy download en

ENTRYPOINT [ "gunicorn", "server:app", "-b 0.0.0.0:5000", "-w 2", "-t 5", "--preload"]

 