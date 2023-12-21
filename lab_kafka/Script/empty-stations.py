#! /usr/bin/env python3
import json
from kafka import KafkaConsumer
from kafka import KafkaProducer


consumer = KafkaConsumer("stations-status", bootstrap_servers='localhost:9092',
                         group_id="velib-monitor-stations")

producer = KafkaProducer(bootstrap_servers="localhost:9092")

for message in consumer:
    station = json.loads(message.value.decode())
    station_id = station["name"]+station["contract_name"]
    available_bikes = station["available_bikes"]
    diff_available_bikes = station["diff_available_bikes"]
    free_slots = station["available_bike_stands"]

    if available_bikes==0:
        station["isEmpty"] = 1
        print(rf" {station['name']} is became empty")
        producer.send("empty-stations", json.dumps(station).encode())
    
    if available_bikes==1 and diff_available_bikes>0:
        station["isEmpty"] = 0
        print(rf" {station['name']} is not empty anymore")
        producer.send("empty-stations", json.dumps(station).encode())

    

    



