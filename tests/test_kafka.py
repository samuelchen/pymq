#!/usr/bin/env python
# coding: utf-8

"""
Tests for MQ
"""

import unittest
from mq.consts import MQTypes, KafkaConfKeys
from mq.factory import MQClientFactory
from tests import read_conf


class KafkaTestCase(unittest.TestCase):
    def setUp(self):
        self.mqtype = MQTypes.Kafka
        self.conf = {}
        conf = read_conf('config.ini')
        for k, v in conf.items(MQTypes.Kafka):
            self.conf[k] = v
        self.mq = MQClientFactory.create_connection(self.mqtype, self.conf)
        self.mq.connect()

    def tearDown(self):
        self.mq.disconnect()

    def test_send_to_topic(self):
        msg = 'my first test message.'
        producer = self.mq.create_producer()
        producer.produce(msg, topic=self.mq.config[KafkaConfKeys.topic_out])
        self.assertEqual(True, True)


if __name__ == '__main__':
    unittest.main()
