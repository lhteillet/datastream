# %%

import json
from kafka import KafkaConsumer


consumer = KafkaConsumer("empty-stations", bootstrap_servers='localhost:9092',
                         group_id="velib-monitor-stations")

for message in consumer:
    station = json.loads(message.value.decode())
    if station["isEmpty"]:
        print("Stations located in {} in {} is empty".format(station["address"],station["contract_name"]))
    
