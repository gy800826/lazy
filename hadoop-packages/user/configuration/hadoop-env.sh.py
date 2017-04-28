#!/usr/bin/env python
# -*- coding: UTF-8 -*-
#user

import os

os.system("sed -i '/os.open('export HADOOP_PID_DIR=.home/,$d' /home/hadoop/hadoop-2.8.0/etc/hadoop/hadoop-env.sh")

env = os.open('/home/hadoop/hadoop-2.8.0/etc/hadoop/hadoop-env.sh', os.O_RDWR|os.O_APPEND)
os.write(env,'\n\n')
os.write(env,'export HADOOP_PID_DIR=/home/hadoop/pids\n')
os.write(env,'export JAVA_HOME=/usr/java/java\n')
os.write(env,'export HADOOP_HOME=/home/hadoop/hadoop-2.8.0\n')
os.write(env,'export PATH=$PATH:$HADOOP_HOME/bin\n')
os.write(env,'export PATH=$PATH:$HADOOP_HOME/sbin\n')
os.write(env,'export HADOOP_MAPRED_HOME=$HADOOP_HOME\n')
os.write(env,'export HADOOP_COMMON_HOME=$HADOOP_HOME\n')
os.write(env,'export HADOOP_HDFS_HOME=$HADOOP_HOME\n')
os.write(env,'export YARN_HOME=$HADOOP_HOME\n')
os.write(env,'export HADOOP_COMMON_LIB_NATIVE_DIR=$HADOOP_HOME/lib/native\n')
os.write(env,'export HADOOP_OPTS="-Djava.library.path=$HADOOP_HOME/lib/native"\n')

os.close(env)

print 'env,end'