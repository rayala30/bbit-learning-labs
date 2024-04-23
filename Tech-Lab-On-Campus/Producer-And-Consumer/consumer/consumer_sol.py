# Test File 
# import mqConsumerInterface

import os
import pika

from consumer_interface import mqConsumerInterface

class mqConsumer(mqConsumerInterface):

    def __init__(self):
        mqConsumer = mqConsumer()

        self._binding_key = ""
        self._exchange_name = ""
        self._queue_name = ""
        

    def setupRMQConnection(self):
        pass

    def onMessageCallback(self):
        pass


    def startConsuming(self):
        pass




