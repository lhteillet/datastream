from kafka import KafkaConsumer, KafkaAdminClient
from confluent_kafka.admin import AdminClient
from confluent_kafka import Consumer, TopicPartition
KAFKA_BROKER = "localhost:9092"



#    consumer = KafkaConsumer(bootstrap_servers=bootstrap_servers, group_id=group_id, enable_auto_commit=False)

    # partitions = consumer.partitions_for_topic(topic)
    # topic_partitions = [TopicPartition(topic, partition) for partition in partitions]

    # consumer.assign(topic_partitions)
    # end_offsets = consumer.end_offsets(topic_partitions)

    # for partition, end_offset in end_offsets.items():
    #     current_offset = consumer.position(partition)
    #     print(f"Topic: {topic}, Partition: {partition}, Group: {group_id}, Current Offset: {current_offset}, End Offset: {end_offset}")

def test_monitor():
    a = AdminClient({'bootstrap.servers': KAFKA_BROKER})
    groups = a.list_groups(timeout=10)
    print(" {} consumer groups".format(len(groups)))
    for g in groups:
        print(" \"{}\" with {} member(s), protocol: {}, protocol_type: {}".format(
            g, len(g.members), g.protocol, g.protocol_type))

        for m in g.members:
            print("id {} client_id: {} client_offset: {}".format(m.id, m.client_id, type(m.metadata)))

                    
def monitor_kafka_topics():

    consumer = KafkaConsumer(bootstrap_servers=KAFKA_BROKER)
    topics = consumer.topics()
    admin_client = KafkaAdminClient(bootstrap_servers=KAFKA_BROKER)
    consumer_groups = admin_client.list_consumer_groups()
    for consumer_group in consumer_groups:
        consumer_group_name = consumer_group[0]
        consumer = KafkaConsumer(bootstrap_servers=KAFKA_BROKER,group_id = consumer_group_name)
        #output_to_print = "Consumer groups name : {}, Topics : {}".format(consumer_group_name)
        output_to_print = "Consumer groups name : {} \n     Suscribed Topics : {}"
        topics_info = "\n       "
        for topic in consumer.topics():
            topic_info = rf". {topic}"
            for partition in consumer.partitions_for_topic(topic):
                topic_info += "\n           Partition {} : ".format(str(partition))
            topics_info += topic_info + "\n       "
        output_to_print = output_to_print.format(consumer_group_name,topics_info)
        print(output_to_print)
    #for topic in topics:
        #print("Topic name {}".format(topic))
        #partitions = consumer.partitions_for_topic(topic)
        # for partition in partitions:
            #print("Partitions ID {}".format(partition))
            #partition_info = consumer.seek_to_end(partition=partition)
            # offset = partition_info.offset
            # timestamp = partition_info.timestamp
            # print(f"Topic-name: {topic}, Partition-id: {partition}, Offset-id: {offset}, Timestamp: {timestamp}")

if __name__ == "__main__":
    #monitor_kafka_topics()
    test_monitor()