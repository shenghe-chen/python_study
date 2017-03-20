#!/usr/bin/python
from __future__ import print_function

with open('/root/access.log') as f:
    d={}
    for i in [ line.split()[8] for line in f ]:
        if d.get(i) == None:
            if i not in d:
                d[i]=1
        else:
            d[i]+=1
sum1=0
sum2=0
for i in d:
    if int(i) < 400:
        sum1+=d[i]
    else:
        sum2+=d[i]
print(sum1*1.0/(sum1+sum2))
