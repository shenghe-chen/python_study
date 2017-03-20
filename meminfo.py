#!/usr/bin/python
from __future__ import print_function


with open('/proc/meminfo') as f:
    for i in [ line for line in f if 'Mem' in line]:
        print(i,end='')

