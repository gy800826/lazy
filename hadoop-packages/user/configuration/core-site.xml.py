#!/usr/bin/env python
# -*- coding: UTF-8 -*-
#user

import os

os.system("sed -i '/<configuration>/,$d' /home/hadoop/hadoop-2.8.0/etc/hadoop/core-site.xml")
core = os.open('/home/hadoop/hadoop-2.8.0/etc/hadoop/core-site.xml', os.O_RDWR|os.O_APPEND)
os.write(core,'\n\n')
os.write(core,'<configuration>\n\n')

#namenode:port
os.write(core,'<property>\n')
os.write(core,'<name>fs.default.name</name>\n')
os.write(core,'<value>hdfs://namenode-ip:9000</value>\n')
os.write(core,'</property>\n\n')

#hadoop.tmp.dir
os.write(core,'<property>\n')
os.write(core,'<name>hadoop.tmp.dir</name>\n')
os.write(core,'<value>/home/hadoop/tmp/</value>\n')
os.write(core,'</property>\n\n')

#namesecondary.checkpoint.dir
os.write(core,'<property>\n')
os.write(core,'<name>fs.checkpoint.dir</name>\n')
os.write(core,'<value>/home/hadoop/dfs/namesecondary</value>\n')
os.write(core,'</property>\n\n')

#checkpoint Intervals(s)
os.write(core,'<property>\n')
os.write(core,'<name>fs.checkpoint.period</name>\n')
os.write(core,'<value>300</value>\n')
os.write(core,'</property>\n\n')

#clear trash(hr)
os.write(core,'<property>\n')
os.write(core,'<name>fs.trash.interval</name>\n')
os.write(core,'<value>1440</value>\n')
os.write(core,'</property>\n\n')

#
os.write(core,'<property>\n')
os.write(core,'<name>io.file.buffer.size</name>\n')
os.write(core,'<value>32768</value>\n')
os.write(core,'</property>\n\n')


os.write(core,'\n\n')
os.write(core,'</configuration>')
os.close(core)
#end
print 'core,end'