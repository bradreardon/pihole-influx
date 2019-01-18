# pihole-influx

A simple daemonized script to report Pi-Hole stats to an InfluxDB, ready to be displayed via Grafana.

![Example Grafana Dashboard](.readme-assets/dashboard.png)

## Configuration

This container is configured by a series of environment variables.

|Environment variable|Description|
|---|---|
|`PIHOLE_HOSTNAME`|The Pihole's hostname.|
|`PIHOLE_API`|The API URL of the Pihole on the network.|
|`REPORTING_INTERVAL`|Reporting interval of script. Defaults to every 10 seconds.|
|`INFLUX_HOST`|Host of the InfluxDB server.|
|`INFLUX_PORT`|InfluxDB port. Defaults to `8086`.|
|`INFLUX_USER`|The username for the InfluxDB user|
|`INFLUX_PASSWORD`|The password for the InfluxDB user|
|`INFLUX_DB`|The database name in InfluxDB|

## Set up a Grafana Dashboard 

The example dashboard seen [at the top](#pi-hole-influx) uses the collected data and displays it in concise and sensible graphs and single stats. The dashboard can be imported into your Grafana instance from the `dashboard.json` file included in the repo, or by using ID `6603` to [import it from Grafana's Dashboard Directory](https://grafana.com/dashboards/6603).


## Attributions

Quoted from the README of the forked repo `janw/pi-hole-influx`:
> The script originally [created by Jon Hayward](https://fattylewis.com/Graphing-pi-hole-stats/), adapted to work with InfluxDB [by /u/tollsjo in December 2016](https://github.com/sco01/piholestatus), and [improved and extended by @johnappletree](https://github.com/johnappletree/piholestatus). "If I have seen further it is by standing on the shoulders of giants". 🤓

Further modified by [Brad Reardon](https://github.com/bradreardon) to work with Docker.
