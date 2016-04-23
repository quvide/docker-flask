FROM python:2.7
RUN pip install uwsgi flask 
EXPOSE 9000
COPY app /app
WORKDIR /app
CMD ["uwsgi", "uwsgi.ini"]

