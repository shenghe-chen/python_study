#!/usr/bin/python
from __future__ import print_function
import fnmatch
import tarfile
import shutil
import os


path='/root/python_study/backup_test'
os.chdir(path)
shutil.make_archive('backup','gztar',path)
f = tarfile.open('backup1.tar.gz','w:gz')
for name in [i for i in os.listdir(path) if fnmatch.fnmatch(i,'*.txt')]:
#for name in [i for i in os.listdir(path) if i.endswith('.txt')]:
    f.add(name)
f.close()
