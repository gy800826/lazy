#!/usr/bin/env python
# -*- coding: UTF-8 -*-
#user

import os
os.system("sed -i '/<configuration>/,$d' /home/hadoop/hadoop-2.8.0/etc/hadoop/yarn-site.xml")
yarn = os.open('/home/hadoop/hadoop-2.8.0/etc/hadoop/yarn-site.xml', os.O_RDWR|os.O_APPEND)
os.write(yarn,'\n\n')
os.write(yarn,'<configuration>\n\n')
#
os.write(yarn,'<property>\n')
os.write(yarn,'<name>yarn.resourcemanager.resource-tracker.address</name>\n')
os.write(yarn,'<value>namenode-ip:8031</value>\n')
os.write(yarn,'</property>\n\n')

#
os.write(yarn,'<property>\n')
os.write(yarn,'<name>yarn.resourcemanager.scheduler.address</name>\n')
os.write(yarn,'<value>namenode-ip:8030</value>\n')
os.write(yarn,'</property>\n\n')

#
os.write(yarn,'<property>\n')
os.write(yarn,'<name>yarn.resourcemanager.scheduler.class</name>\n')
os.write(yarn,'<value>org.apache.hadoop.yarn.server.resourcemanager.scheduler.capacity.CapacityScheduler</value>\n\n')
os.write(yarn,'</property>\n\n')

#
os.write(yarn,'<property>\n')
os.write(yarn,'<name>yarn.resourcemanager.address</name>\n')
os.write(yarn,'<value>namenode-ip:8032</value>\n')
os.write(yarn,'</property>\n\n')

#
os.write(yarn,'<property>\n')
os.write(yarn,'<name>yarn.nodemanager.local-dirs</name>\n')
os.write(yarn,'<value>/home/hadoop/tmp/nodemanager/local</value>\n')
os.write(yarn,'</property>\n\n')

#
os.write(yarn,'<property>\n')
os.write(yarn,'<name>yarn.nodemanager.address</name>\n')
os.write(yarn,'<value>0.0.0.0:8034</value>\n')
os.write(yarn,'</property>\n\n')

#
os.write(yarn,'<property>\n')
os.write(yarn,'<name>yarn.nodemanager.remote-app-log-dir</name>\n')
os.write(yarn,'<value>/logs</value>\n')
os.write(yarn,'</property>\n\n')

#
os.write(yarn,'<property>\n')
os.write(yarn,'<name>yarn.nodemanager.log-dirs</name>\n')
os.write(yarn,'<value>/home/hadoop/hadoop-2.8.0/nodemanager/logs</value>\n')
os.write(yarn,'</property>\n\n')

#
os.write(yarn,'<property>\n')
os.write(yarn,'<name>yarn.nodemanager.aux-services</name>\n')
os.write(yarn,'<value>mapreduce_shuffle</value>\n')
os.write(yarn,'</property>\n\n')

#
os.write(yarn,'<property>\n')
os.write(yarn,'<name>yarn.nodemanager.aux-services.mapreduce.shuffle.class</name>\n')
os.write(yarn,'<value>org.apache.hadoop.mapred.ShuffleHandler</value>\n')
os.write(yarn,'</property>\n\n')

#
os.write(yarn,'<property>\n')
os.write(yarn,'<name>yarn.log-aggregation-enable</name>\n')
os.write(yarn,'<value>true</value>\n')
os.write(yarn,'<description>Configuration to enable or disable log aggregation</description>\n')
os.write(yarn,'</property>\n\n')
os.write(yarn,'</configuration>\n\n')
os.close(yarn)


print 'yarn,end'