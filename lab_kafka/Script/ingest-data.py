# %%
import requests
from kafka import KafkaProducer
import time 
import urllib.request
import json


url = "https://api.jcdecaux.com/vls/v1/stations?apiKey=7b652e33616f8f27d947f36405bd3dc9cf8a8bb3"

while True:


    producer = KafkaProducer(bootstrap_servers="localhost:9092")
    topic_name = "velib-stations"
    response = urllib.request.urlopen(url)
    stations = json.loads(response.read().decode())
    for station in stations:
        producer.send("velib-stations", json.dumps(station).encode())
    print("{} Produced {} station records".format(time.time(), len(stations)))


    time.sleep(10)


# %%



