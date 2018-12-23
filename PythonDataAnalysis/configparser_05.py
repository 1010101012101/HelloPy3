# -*- coding: utf-8 -*-
"""
Created on Mon Mar 12 12:55:11 2018

@author: mc.meng
"""

import configparser


def opt_move(config, section1, section2, option):
    try:
        config.set(section2, option, config.get(section1, option, raw=True))
    except configparser.NoSectionError:
        # Create non-existent section
        config.add_section(section2)
        opt_move(config, section1, section2, option)
    else:
        config.remove_option(section1, option)
        
config = configparser.ConfigParser()
config.read('example.cfg')
opt_move(config, "Section1", "Section2", "foo")
#config.write("example.cfg")
with open('example.cfg', 'w') as configfile:
    config.write(configfile)