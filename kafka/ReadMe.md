

/*Start kafka and zookeeper*/

bin/zookeeper-server-start.sh config/zookeeper.properties

bin/kafka-server-start.sh config/server.properties

/*Remove records from topic*/
./bin/kafka-delete-records.sh --bootstrap-server localhost:9092 --offset-json-file ./offsetfile.json