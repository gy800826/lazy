#!/usr/bin/env python
# -*- coding: UTF-8 -*-
#root
import os


#install jdk
os.system('wget --no-cookies --no-check-certificate --header \
"Cookie: gpw_e24=http%3A%2F%2Fwww.oracle.com%2F; oraclelicense=accept-securebackup-cookie" \
"http://download.oracle.com/otn-pub/java/jdk/7u79-b15/jdk-7u79-linux-x64.rpm"')
os.system('rpm -ivh jdk-7u79-linux-x64.rpm')


#java link
os.system('ln -s /usr/java/jdk1.7.0_79/ /usr/java/java')


#java path
profile = os.open('/etc/profile', os.O_RDWR|os.O_APPEND)
os.write(profile,'\n\n\n\n')
os.write(profile,'export JAVA_HOME=/usr/java/java\n')
os.write(profile,'export JRE_HOME=$JAVA_HOME/jre\n')
os.write(profile,'export CLASSPATH=.:$JAVA_HOME/lib/dt.jar:$JAVA_HOME/lib/tools.jar:$JRE_HOME/lib/rt.jar\n')
os.write(profile,'export export PATH=$PATH:$JAVA_HOME/bin\n')


os.write(profile,'\n\n\n\n')
os.write(profile,'export HADOOP_HOME=/home/hadoop/hadoop-2.8.0/\n')
os.write(profile,'export HADOOP_MAPRED_HOME=$HADOOP_HOME\n')
os.write(profile,'export HADOOP_COMMON_HOME=$HADOOP_HOME\n')
os.write(profile,'export HADOOP_HDFS_HOME=$HADOOP_HOME\n')
os.write(profile,'export YARN_HOME=$HADOOP_HOME\n')
os.write(profile,'export HADOOP_CONF_DIR=$HADOOP_HOME/etc/hadoop\n')
os.write(profile,'export YARN_CONF_DIR=$HADOOP_HOME/etc/hadoop\n')
os.write(profile,'export PATH=$PATH:$HADOOP_HOME/bin:$HADOOP_HOME/sbin\n')
os.close(profile)

os.system('source /etc/profile')

#setup safety
os.system('setenforce 0')


#stop selinux 
os.system("sed -i 's/SELINUX=enforcing/SELINUX=disabled/g' /etc/selinux/config")


#stop iptables
os.system('service iptables stop')
os.system('chkconfig iptables off')


#setup SSH don't ask
os.system("sed -i 's/#   StrictHostKeyChecking ask/StrictHostKeyChecking no/g' /etc/ssh/ssh_config")
os.system('service sshd restart ')

#date
os.system("sed -i 's/America/Asia/g' /etc/sysconfig/clock")
os.system("sed -i 's/Los_Angeles/Taipei/g' /etc/sysconfig/clock")
os.system('cp /usr/share/zoneinfo/Asia/Taipei /etc/localtime')
os.system('hwclock -r ; hwclock -w')

#start ntpd
os.system('chkconfig ntpd on')
os.system('service ntpd start')

#set hosts
os.system('cat /home/hadoop/hadoop-packages/root/config_hosts.txt >> /etc/hosts')

print  'finsh'