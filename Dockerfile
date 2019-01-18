FROM python:3.7
COPY . /data/app
CMD python /data/app/piholeinflux.py