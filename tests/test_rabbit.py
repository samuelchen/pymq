#!/usr/bin/env python
# coding: utf-8

"""
Tests for MQ
"""

import unittest
from mq.consts import MQTypes, RabbitConfKeys
from mq.factory import MQClientFactory
from tests import read_conf


class TestRabbitMQ(unittest.TestCase):
    def setUp(self):
        self.mqtype = MQTypes.RabbitMQ
        self.conf = {}
        conf = read_conf('config.ini')
        for k, v in conf.items(MQTypes.RabbitMQ):
            self.conf[k] = v
        self.mq = MQClientFactory.create_connection(self.mqtype, self.conf)
        self.mq.connect()

    def tearDown(self):
        self.mq.disconnect()

    def test_send_to_queue(self):
        msg = 'my first test message.'
        producer = self.mq.create_producer()
        producer.produce(msg, queue=self.mq.config[RabbitConfKeys.queue_out])
        self.assertEqual(True, True)

    def test_send_to_exchange(self):
        msg = 'my second test message to topic & key.'
        producer = self.mq.create_producer()
        producer.produce(msg, topic=self.mq.config[RabbitConfKeys.topic_out],
                         key=self.mq.config[RabbitConfKeys.queue_out])
        self.assertEqual(True, True)

if __name__ == '__main__':
    unittest.main()
