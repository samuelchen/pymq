#!/usr/bin/env python
# coding: utf-8

"""
Some constants
"""
from .utils import MutableEnum


MQTypes = MutableEnum(
    RabbitMQ='RabbitMQ',
    Kafka='Kafka'
)

# RabbitMQ config keys. initialize with order
RabbitConfKeys = MutableEnum([
    ('host', 'rabbit_host'),
    ('port', 'rabbit_port'),
    ('vhost', 'rabbit_vhost'),
    ('user', 'rabbit_user'),
    ('password', 'rabbit_password'),

    ('queue_in', 'rabbit_default_consuming_queue'),
    ('queue_out', 'rabbit_default_producing_queue'),
    ('topic_in', 'rabbit_default_consuming_topic_of_exchange'),
    ('topic_out', 'rabbit_default_producing_topic_of_exchange'),
    ('key_in', 'rabbit_default_consuming_key_for_topic_exchange'),
    ('key_out', 'rabbit_default_producing_key_for_topic_exchange'),
])

# Kafka config keys. initialize with order
KafkaConfKeys = MutableEnum([
    ('host', 'kafka_host'),
    ('port', 'kafka_port'),
    # ('user', 'kafka_user'),
    # ('password', 'kafka_password'),

    ('topic_in', 'kafka_default_consuming_topic'),
    ('topic_out', 'kafka_default_producing_topic'),
])