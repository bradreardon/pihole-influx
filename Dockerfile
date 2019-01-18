FROM python:3.7
COPY requirements.txt /data/app/requirements.txt
RUN pip install -r /data/app/requirements.txt
COPY piholeinflux.py /data/app/piholeinflux.py
CMD python /data/app/piholeinflux.py