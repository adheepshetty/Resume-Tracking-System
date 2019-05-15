#from kafka import KafkaProducer
import json
#producer = KafkaProducer(value_serializer=lambda v: json.dumps(v).encode('utf-8'))
#producer.send('test', {'foo': 'bar'})

list2=json.loads(gen_resume(idd, driver).toJSON())
