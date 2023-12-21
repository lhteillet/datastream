import json
from kafka import KafkaConsumer


consumer = KafkaConsumer("velib-stations", bootstrap_servers='localhost:9092',
                         group_id="velib-archive-stations")





f = open("archive_data.txt", "a")
try:
    for message in consumer:
        station = json.loads(message.value.decode())
        f.write(json.dumps(station))
        print("Wrote message for station {}".format(station["name"]))

except KeyboardInterrupt:
    print("Interrupted by user")
    consumer.close()
    f.close()
    
      