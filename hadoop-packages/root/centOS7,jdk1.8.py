#!/usr/bin/env python
# -*- coding: UTF-8 -*-
#root
import os


#install jdk
os.system('wget --no-cookies --no-check-certificate --header \
"Cookie: gpw_e24=http%3A%2F%2Fwww.oracle.com%2F; oraclelicense=accept-securebackup-cookie" \
"http://download.oracle.com/otn-pub/java/jdk/8u121-b13/e9e7ea248e2c4826b92b3f075a80e441/jdk-8u121-linux-x64.rpm"')
os.system('rpm -ivh jdk-8u121-linux-x64.rpm')


#java link
os.system('ln -s /usr/java/jdk1.8.0_121/ /usr/java/java')


#java path
profile = os.open('/etc/profile', os.O_RDWR|os.O_APPEND)
os.write(profile,'\n\n\n\n')
os.write(profile,'export JAVA_HOME=/usr/java/java\n')
os.write(profile,'export JRE_HOME=$JAVA_HOME/jre\n')
os.write(profile,'export CLASSPATH=.:$JAVA_HOME/lib/dt.jar:$JAVA_HOME/lib/tools.jar:$JRE_HOME/lib/rt.jar\n')
os.write(profile,'export export PATH=$PATH:$JAVA_HOME/bin\n')

os.write(profile,'\n\n\n\n')
os.write(profile,'export HADOOP_HOME=/home/hadoop/hadoop-2.8.0\n')
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


#stop firewalld
os.system('systemctl stop firewalld.service')
os.system('systemctl disable firewalld.service')


#setup SSH don't ask
os.system("sed -i 's/#   StrictHostKeyChecking ask/StrictHostKeyChecking no/g' /etc/ssh/ssh_config")
os.system('systemctl restart sshd')



#install ntp
#install packages
os.system('yum install -y ntp')
os.system('yum install -y ntp ntpdate ntp-doc')
#BOOT and start NTP Daemon
os.system('systemctl enable ntpd')
#systemtime and pool.ntp.org NTP server on timing
os.system('ntpdate pool.ntp.org')
#start NTP Daemon
os.system('systemctl start ntpd')

#date
os.system('timedatectl set-timezone "Asia/Taipei"')
os.system('hwclock -r ; hwclock -w')

#set hosts
os.system('cat /home/hadoop/hadoop-packages/root/config_hosts.txt >> /etc/hosts')

print  'finsh'