#! /usr/bin/env python3
import json
from kafka import KafkaConsumer
from kafka import KafkaProducer

stations = {}
consumer = KafkaConsumer("velib-stations", bootstrap_servers='localhost:9092',
                         group_id="velib-monitor-stations")

producer = KafkaProducer(bootstrap_servers="localhost:9092")
for message in consumer:
    station = json.loads(message.value.decode())
    station_id = station["name"]+station["contract_name"]
    available_bikes = station["available_bikes"]
    free_slots = station["available_bike_stands"]

    # if station_id=="STORTORGET":
    #     print(station)
    if station_id not in stations:
        stations[station_id] = [available_bikes,free_slots]


    diff_available_bikes = available_bikes - stations[station_id][0]
    diff_free_slots = free_slots - stations[station_id][1]

    if diff_available_bikes != 0 or diff_free_slots != 0:
        station["diff_available_bikes"] = diff_available_bikes
        station["diff_free_slots"] = diff_free_slots
        producer.send("stations-status", json.dumps(station).encode())
        print("{}{} free slots at station {}".format(
            "+" if diff_free_slots > 0 else "",
            diff_free_slots, station["name"]
        ))
        stations[station_id] = [available_bikes,free_slots]

