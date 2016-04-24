FROM python:3.5
RUN pip install uwsgi flask 
EXPOSE 9000
COPY app /app
WORKDIR /app
CMD ["uwsgi", "uwsgi.ini"]

