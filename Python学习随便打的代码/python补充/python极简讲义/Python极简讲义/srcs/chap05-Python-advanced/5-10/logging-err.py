#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct  1 16:25:06 2019

@author: yhilly
"""

import logging
logging.basicConfig(level=logging.INFO)

def foo(s):
    n = int(s)
    logging.info('n = {}'.format(n))
    return 10 / n


foo('0')


