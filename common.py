#!/usr/bin/env python3
# -*- coding: utf8 -*-

import logging
import os
from configparser import ConfigParser

logger = logging.getLogger('workflows')

def getConf():
    logger = logging.getLogger(__name__)
    logger.info('%s.getConf starts', __name__)
    currentPath = os.path.dirname(os.path.abspath(__file__))
    cfg = ConfigParser()
    confPath = currentPath + '/conf/smartclonner.conf'
    try:
        cfg.read(confPath)
    except Exception as e:
        print(e)
    return cfg

def setConf(cfg):
    currentPath = os.path.dirname(os.path.abspath(__file__))
    confPath = currentPath + '/conf/smartclonner.conf'
    try:
        with open(confPath, 'w') as configfile:
            cfg.write(configfile)
    except Exception as e:
        print(e)