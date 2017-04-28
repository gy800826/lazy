#!/usr/bin/env python
# -*- coding: UTF-8 -*-
#user

import os
os.system("sed -i '/<configuration>/,$d' /home/hadoop/hadoop-2.8.0/etc/hadoop/hdfs-site.xml")
hdfs = os.open('/home/hadoop/hadoop-2.8.0/etc/hadoop/hdfs-site.xml', os.O_RDWR|os.O_APPEND)
os.write(hdfs,'\n\n')
os.write(hdfs,'<configuration>\n\n')

#replication
os.write(hdfs,'<property>\n')
os.write(hdfs,'<name>dfs.replication</name>\n')
os.write(hdfs,'<value>2</value>\n')
os.write(hdfs,'</property>\n\n')

#replication.min
os.write(hdfs,'<property>\n')	
os.write(hdfs,'<name>dfs.replication.min</name>\n')
os.write(hdfs,'<value>2</value>\n')
os.write(hdfs,'</property>\n\n')

#permissions
os.write(hdfs,'<property>\n')
os.write(hdfs,'<name>dfs.permissions</name>\n')
os.write(hdfs,'<value>false</value>\n')
os.write(hdfs,'</property>\n\n')

#namenodeip web-UI
os.write(hdfs,'<property>\n')
os.write(hdfs,'<name>dfs.http.address</name>\n')
os.write(hdfs,'<value>namenode-ip:50070</value>\n')
os.write(hdfs,'</property>\n\n')

#blocksize
os.write(hdfs,'<property>\n')
os.write(hdfs,'<name>dfs.block.size</name>\n')
os.write(hdfs,'<value>134217728</value>\n')
os.write(hdfs,'</property>\n\n')

#heartbeat(s)
os.write(hdfs,'<property>\n')
os.write(hdfs,'<name>dfs.heartbeat.interval</name>\n')
os.write(hdfs,'<value>3</value>\n')
os.write(hdfs,'</property>\n\n')

#
os.write(hdfs,'<property>\n')
os.write(hdfs,'<name>dfs.datanode.directoryscan.threads</name>\n')
os.write(hdfs,'<value>48</value>\n')
os.write(hdfs,'</property>\n\n')

#
os.write(hdfs,'<property>\n')
os.write(hdfs,'<name>dfs.datanode.max.xcievers</name>\n')
os.write(hdfs,'<value>4096</value>\n')
os.write(hdfs,'</property>\n\n')

#exclude datanode-ip
os.write(hdfs,'<property>\n')        
os.write(hdfs,'<name>dfs.hosts.exclude</name>\n')
os.write(hdfs,'<value>/home/hadoop/hadoop-2.8.0/etc/hadoop/exclude_node</value>\n')  
os.write(hdfs,'</property>\n\n')

#bandwidthPerSec(b/s)
os.write(hdfs,'<property>\n')
os.write(hdfs,'<name>dfs.balance.bandwidthPerSec</name>\n')
os.write(hdfs,'<value>31457280</value>\n')
os.write(hdfs,'</property>\n\n')

#
os.write(hdfs,'<property>\n')
os.write(hdfs,'<name>dfs.datanode.handler.count</name>\n')
os.write(hdfs,'<value>20</value>\n')
os.write(hdfs,'</property>\n\n')

#
os.write(hdfs,'<property>\n')
os.write(hdfs,'<name>dfs.namenode.handler.count</name>\n')
os.write(hdfs,'<value>50</value>\n')
os.write(hdfs,'</property>\n\n')

#datanode check block(hr)
os.write(hdfs,'<property>\n')
os.write(hdfs,'<name>dfs.datanode.scan.period.hours</name>\n')
os.write(hdfs,'<value>168</value>\n')
os.write(hdfs,'</property>\n\n')

#
os.write(hdfs,'<property>\n')
os.write(hdfs,'<name>dfs.datanode.socket.write.timeout</name>\n')
os.write(hdfs,'<value>600000</value>\n')
os.write(hdfs,'</property>\n\n')

#
os.write(hdfs,'<property>\n')
os.write(hdfs,'<name>dfs.socket.timeout</name>\n')
os.write(hdfs,'<value>600000</value>\n')
os.write(hdfs,'</property>\n\n')

#
os.write(hdfs,'<property>\n')
os.write(hdfs,'<name>dfs.support.append</name>\n')
os.write(hdfs,'<value>true</value>\n')
os.write(hdfs,'</property>\n\n')

os.write(hdfs,'</configuration>\n')
os.close(hdfs)


#end
print 'hdfs,end'