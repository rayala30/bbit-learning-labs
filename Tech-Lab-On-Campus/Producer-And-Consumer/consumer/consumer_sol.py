# Test File 
# import mqConsumerInterface

import os
import pika

from consumer_interface import mqConsumerInterface

class mqConsumer(mqConsumerInterface):

    def __init__(self, binding_key: str, exchange_name: str, queue_name: str):
        self._binding_key = binding_key
        self._exchange_name = exchange_name
        self._queue_name = queue_name
        # Call setupRMQConnection here 
        self.setupRMQConnection()
        

    def setupRMQConnection(self):
        # Setup connection 
        con_params = pika.URLParameters(os.environ["AMQP_URL"])
        connection = pika.BlockingConnection(parameters=con_params)

        # Create a channel
        channel = connection.channel()

        # Create a queue
        queue_start = channel.queue_declare(queue=self._queue_name)

        # Create the exchange 
        exchange_start = channel.exchange_declare(exchange=self._exchange_name)

        # Bind binding key
        channel.queue_bind(
        queue= queue_start,
        routing_key= self._binding_key,
        exchange=exchange_start,
        )

        # Setup callback function 
        channel.basic_consume(self._queue_name, self.setupRMQConnection(), 
                              auto_ack=False)
        
        

    def on_message_callback(self, channel, method_frame, header_frame, body):
        # Acknowledge message
        channel.basic_ack(method_frame.delivery_tag, False)

        # Print body message
        print(body)

    def startConsuming(self):
        print("[*] Waiting for messages. To exit press CTRL+C")

        # Start consuming messages
        channel.start_consuming()

    def __del__(self):
        print("Closing RMQ connection on destruction")

        # Close channel
        channel.close()
        # Close connection 
        connection.close()
        




