Up zookeeper : ./bin/zookeeper-server-start.sh config/zookeeper.properties
Up server : ./bin/kafka-server-start.sh config/server.properties
CAC40 activity : ./bin/kafka-console-consumer.sh --topic valib_station --bootstrap-server localhost:9092
List of topics : ./bin/kafka-topics.sh --list --bootstrap-server localhost:9092
Manualy create topic : ./bin/kafka-topics.sh --create --topic velib-stations --partitions 2 --replication-factor 1 --bootstrap-server localhost:9092


# For louisteillet


## Start the ZooKeeper service - Terminal 1
cd /Users/louisteillet/kafka_2.13-3.6.0
bin/zookeeper-server-start.sh config/zookeeper.properties

## Start the Kafka broker service  - Terminal 2
cd /Users/louisteillet/kafka_2.13-3.6.0
bin/kafka-server-start.sh config/server.properties

## Manually create a topic - Terminal 3
cd /Users/louisteillet/kafka_2.13-3.6.0
./bin/kafka-topics.sh --create --topic velib_stations --partitions 1 --replication-factor 1 --bootstrap-server localhost:9092

## Describe topics - Terminal 3
bin/kafka-topics.sh --describe --topic velib-stations --bootstrap-server localhost:9092

## List of topics
cd /Users/louisteillet/kafka_2.13-3.6.0
./bin/kafka-topics.sh --list --bootstrap-server localhost:9092

## Monitor topics
./bin/kafka-console-consumer.sh --topic cac40-5min --bootstrap-server localhost:9092
./bin/kafka-console-consumer.sh --topic ggstock-5min --bootstrap-server localhost:9092

# Remove topic
cd /Users/louisteillet/kafka_2.13-3.6.0
./bin/kafka-topics.sh --bootstrap-server localhost:9092 --delete --topic valib_stations

## Write some events into the topic - Terminal 4
cd /Users/louisteillet/kafka_2.13-3.6.0
bin/kafka-console-producer.sh --topic cac40-5min  --bootstrap-server localhost:9092
This is my first event
This is my second event

## Read events - Terminal 5
cd /Users/louisteillet/kafka_2.13-3.6.0
bin/kafka-console-consumer.sh --topic cac40-5min --from-beginning --bootstrap-server localhost:9092
This is my first event
This is my second event

# Read description of consumer-group
cd /Users/louisteillet/kafka_2.13-3.6.0
bin/kafka-consumer-groups.sh --bootstrap-server localhost:9092 --describe --group "velib-monitor-stations"  --offsets

# Read description of all consumer-group
./bin/kafka-consumer-groups.sh --bootstrap-server localhost:9092 --all-groups --describe

# remove a consumer-group
cd /Users/louisteillet/kafka_2.13-3.6.0
bin/kafka-consumer-groups.sh --bootstrap-server localhost:9092 --delete --group user

