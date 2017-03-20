#!/usr/bin/python
from __future__ import print_function
import sys
import os


if len(sys.argv[:]) == 1:
    raise SystemExit('Please input source file')
f=sys.argv[1]
if os.path.exists(f):
    if os.access(f,os.R_OK) == False:
        raise SystemExit('Permission denied')
else:
    raise SystemExit('File '+ f +' does not exists')
l=[]
with open(f) as t:
    for line in t.readlines():
        l.extend(' '.join(line.strip().replace('"','').split(':')).split())
num = len([ i for i in ''.join(l) if i=='/'])
l=' '.join((' '.join(l).split('/'))).split()
d={'/':num}
for i in l:
    if d.get(i) != None:
        d[i] += 1
    else:
        d[i] = 1
for k in d:
    print(k,d[k],sep=':',end=' ')
