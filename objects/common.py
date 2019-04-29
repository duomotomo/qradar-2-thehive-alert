#!/usr/bin/env python3
# -*- coding: utf8 -*-

import logging
import os
import re
from configparser import ConfigParser

logger = logging.getLogger('workflows')

def getConf():
    logger = logging.getLogger(__name__)
    logger.info('%s.getConf starts', __name__)
    currentPath = os.path.dirname(os.path.abspath(__file__))
    cfg = ConfigParser(comment_prefixes='#', allow_no_value=True)
    confPath = currentPath + '/../conf/smartclonner.conf'
    print(confPath)
    try:
        cfg.read(confPath)
    except Exception as e:
        print(e)
    return cfg

def setConf(cfg):
    logger = logging.getLogger(__name__)
    logger.info('%s.setConf starts', __name__)
    currentPath = os.path.dirname(os.path.abspath(__file__))
    confPath = currentPath + '/../conf/smartclonner.conf'
    comments_map = save_comments(confPath)
    try:
        with open(confPath, 'w') as configfile:
            cfg.write(configfile)
    except Exception as e:
        print(e)
    restore_comments(confPath, comments_map)

def save_comments(config_file):
    comment_map = {}
    with open(config_file, 'r') as file:
        i = 0
        lines = file.readlines()
        for line in lines:
            if re.match( r'^\s*#.*?$', line):
                comment_map[i] = line
            i += 1
    return comment_map

def restore_comments(config_file, comment_map):
    with open(config_file, 'r') as file:
        lines = file.readlines()
    for (index, comment) in sorted(comment_map.items()):
        lines.insert(index, comment)
    with open(config_file, 'w') as file:
        file.write(''.join(lines))