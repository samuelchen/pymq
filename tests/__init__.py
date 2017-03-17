#!/usr/bin/env python
# coding: utf-8

try:
    import configparser
except ImportError:
    import ConfigParser as configparser


def read_conf(name='config.ini'):
    conf = configparser.ConfigParser()
    conf.read(name)
    return conf