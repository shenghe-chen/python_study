#!/usr/bin/python
import os
from __future__ import print_function


res = len([i for i in os.listdir('/proc') if i.isdigit()])
print(len)
