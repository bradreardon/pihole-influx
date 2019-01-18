#! /usr/bin/python

from __future__ import print_function
import requests
import logging
from time import sleep, localtime, strftime
from influxdb import InfluxDBClient
import os
import traceback
from datetime import datetime
import sys

HOSTNAME = os.env['PIHOLE_HOSTNAME']
PIHOLE_API = HOSTNAME = os.env['PIHOLE_API']
DELAY = int(os.env.get('REPORTING_INTERVAL', 10))

INFLUXDB_SERVER = os.env['INFLUX_HOST']
INFLUXDB_PORT = int(os.env.get('INFLUX_PORT', 8086))
INFLUXDB_USERNAME = os.env['INFLUX_USER']
INFLUXDB_PASSWORD = os.env['INFLUX_PASSWORD']
INFLUXDB_DATABASE = os.env['INFLUX_DB']

INFLUXDB_CLIENT = InfluxDBClient(INFLUXDB_SERVER,
                                 INFLUXDB_PORT,
                                 INFLUXDB_USERNAME,
                                 INFLUXDB_PASSWORD,
                                 INFLUXDB_DATABASE)

logger = logging.get_logger()
logger.info("pihole-influx ready")

def send_msg(resp):
    if 'gravity_last_updated' in resp:
        del resp['gravity_last_updated']

    json_body = [
        {
            "measurement": "pihole",
            "tags": {
                "host": HOSTNAME
            },
            "fields": resp
        }
    ]

    INFLUXDB_CLIENT.write_points(json_body)


if __name__ == '__main__':
    while True:
        try:
            api = requests.get(PIHOLE_API)  # URI to pihole server api
            send_msg(api.json())
            timestamp = strftime('%Y-%m-%d %H:%M:%S %z', localtime())
            logger.info('Reported to InfluxDB at {}'.format(timestamp))

        except Exception as e:
            logger.error('Failed to report to InfluxDB: {}'.format(str(e)))
            print(msg, str(e))
            print(traceback.format_exc())
            sys.exit(1)

        sleep(DELAY)
