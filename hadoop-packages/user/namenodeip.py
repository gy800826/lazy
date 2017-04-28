#!/usr/bin/env python
# -*- coding: UTF-8 -*-
#user

import os
import sys
NI = sys.argv[1]

print NI
#NI = raw_input('namenodeip:')

ipstr = "sed -i 's/namenode-ip/{}/g' /home/hadoop/hadoop-packages/user/configuration/*".format(NI)
#maperd-site.xml.py    hdfs-site.xml.py    core-site.xml.py    #yarn-site.xml.py

os.system(ipstr)
print 'namenodeip end'
