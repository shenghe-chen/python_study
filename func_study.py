#!/usr/bin/python
#coding=utf-8
from __future__ import print_function


#reduce\lambda函数
print(reduce(lambda x,y:x*10+y,(1,2,3,4,5,6)))

#递归函数
def jc(n):
    if n == 1:
        rs = 1
    else:
        rs = jc(n-1) * n
    return rs
print(jc(6))

#map函数
print(map(lambda x:x+2,range(8)))

#filter函数
print(filter(lambda x: x%2 == 0, range(9)))

#回调函数实现map函数
def maptest(fun,seq):
    res=[]
    for i in seq:
        res.append(fun(i))
    return res

def test1(x):
    return x+2

print(test1(1))
print(maptest(test1,range(6)))

#回调函数实现reduce函数
def reducetest(fun,seq):
    res = seq[0]
    for i in seq[1:]:
        res = fun(res,i)
    return res

def test2(x,y):
    return x*10 + y
print(reducetest(test2,(1,2,3,4,5,6)))

#生成器
def gensquares(n):
    for i in range(n):
        yield i * i
l = gensquares(9)
print(l.next())
print(l.next())
print(l.next())
print(l.next())
print(l.next())
print(l.next())
print(l.next())
print(l.next())
print(l.next())
#生成器表达式
l1=(i*i for i in range(9))
print(next(l1))
print(next(l1))
print(next(l1))
print(next(l1))
print(next(l1))
print(next(l1))
print(next(l1))
print(next(l1))
print(next(l1))
