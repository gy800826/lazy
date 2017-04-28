#!/usr/bin/env python
# -*- coding: UTF-8 -*-
#user

import os

os.system('ssh-keygen -t rsa -f ~/.ssh/id_rsa -P ""')
os.system('cat ~/.ssh/id_rsa.pub >> ~/.ssh/authorized_keys')


#download hadoop-2.8.0
os.system('wget http://ftp.twaren.net/Unix/Web/apache/hadoop/common/hadoop-2.8.0/hadoop-2.8.0.tar.gz')

#tar hadoop-2.8.0
os.system('tar zxvf hadoop-2.8.0.tar.gz')
os.system('cp /home/hadoop/hadoop-2.8.0/etc/hadoop/mapred-site.xml.template /home/hadoop/hadoop-2.8.0/etc/hadoop/mapred-site.xml')

#simplify
os.system("sed -i '/os.open('export HADOOP_PID_DIR=.home/,$d' /home/hadoop/hadoop-2.8.0/etc/hadoop/hadoop-env.sh")
os.system('touch /home/hadoop/hadoop-2.8.0/etc/hadoop/exclude_node')

os.system('python /home/hadoop/hadoop-packages/user/configuration/hadoop-env.sh.py')
os.system('python /home/hadoop/hadoop-packages/user/configuration/core-site.xml.py')
os.system('python /home/hadoop/hadoop-packages/user/configuration/hdfs-site.xml.py')
os.system('python /home/hadoop/hadoop-packages/user/configuration/maperd-site.xml.py')
#Not finished
os.system('python /home/hadoop/hadoop-packages/user/configuration/yarn-site.xml.py')

os.system("sed -i 's/os.system/#os.system/g' /home/hadoop/hadoop-packages/user/hadoop-2.8.0.py")

print  'finsh'