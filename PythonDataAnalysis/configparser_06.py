# -*- coding: utf-8 -*-
"""
Created on Mon Mar 12 13:11:46 2018

@author: mc.meng
"""

import configparser
import io

sample_config = """
    [mysqld]
    user = mysql
    pid-file = /var/run/mysqld/mysqld.pid
    skip-external-locking
    old_passwords = 1
    skip-bdb
    skip-innodb
    """

config = configparser.RawConfigParser(allow_no_value=True)
config.read_file(io.StringIO(sample_config))

# Settings with values are treated as before:
print(config.get("mysqld", "user"))

# Settings without values provide None:
print(config.get("mysqld", "skip-bdb"))

# Settings which aren't specified still raise an error:
print(config.get("mysqld", "does-not-exist"))