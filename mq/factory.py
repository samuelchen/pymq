#!/usr/bin/env python
# coding: utf-8
"""
mq modules defines Message Queue clients and some tools.

"""

from .rabbit import RabbitMQConnection
from .kafka import KafkaConnection
from .consts import MQTypes


class MQClientFactory():

    def __init__(self, mq_type):
        self._mq_type = mq_type
        if mq_type not in MQTypes.values:
            raise RuntimeError('Unsupported MQ type "%s"' % mq_type)

    @staticmethod
    def create_connection(mq_type, conf):
        """
        A factory for MQ Connection
        :param mq_type: Message queue type from MQTypes
        :param conf: The configuration dict
        :return:
        """
        conn = None
        if mq_type == MQTypes.RabbitMQ:
            conn = RabbitMQConnection(conf)
        elif mq_type == MQTypes.Kafka:
            conn = KafkaConnection(conf)
        else:
            raise RuntimeError('Unsupported MQ type "%s"' % mq_type)

        # assign methods
        conn.mq_type = mq_type
        # conn.create_producer = MQClientFactory.__create_producer
        # conn.create_consumer = MQClientFactory.__create_consumer
        return conn

    @staticmethod
    def create_producer(mq_type, conf):
        """
        Create a MQ producer instance.
        :param mq_type:
        :param conf:
        :return:
        """
        conn = MQClientFactory.create_connection(mq_type, conf)
        producer = conn.create_producer()
        return producer

    @staticmethod
    def create_consumer(mq_type, conf):
        """
        Create a MQ consumer instance.
        :param mq_type:
        :param conf:
        :return:
        """
        conn = MQClientFactory.create_connection(mq_type, conf)
        producer = conn.create_consumer()
        return producer
