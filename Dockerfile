FROM python:3.6

RUN git clone --branch=pr10 https://github.com/TimofeyBelikov/Practice9_Second.git /rest_second
WORKDIR /rest_second
RUN git fetch

RUN git pull origin pr10
RUN git pull

RUN pip install -r requirements.txt
RUN pip install psycopg2-binary==2.8.6
VOLUME /rest_first

#EXPOSE 8000
WORKDIR /rest_second
CMD python manage.py makemigrations && python manage.py migrate && python manage.py runserver 0.0.0.0:80
