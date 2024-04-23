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
        queue = channel.queue_declare(queue=self._queue_name)

        

    def on_message_callback(self):
        pass


    def startConsuming(self):
        pass




