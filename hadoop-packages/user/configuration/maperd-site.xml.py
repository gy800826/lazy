#!/usr/bin/env python
# -*- coding: UTF-8 -*-
#user

import os
os.system("sed -i '/<configuration>/,$d' /home/hadoop/hadoop-2.8.0/etc/hadoop/mapred-site.xml")
maperd = os.open('/home/hadoop/hadoop-2.8.0/etc/hadoop/mapred-site.xml', os.O_RDWR|os.O_APPEND)

os.write(maperd,'\n\n')
os.write(maperd,'<configuration>\n')
os.write(maperd,'<property>\n')
os.write(maperd,'<name>mapreduce.framework.name</name>\n')
os.write(maperd,'<value>yarn</value>\n')
os.write(maperd,'</property>\n\n')
os.write(maperd,'</configuration>\n')
os.close(maperd)



#end
print 'maperd,end'