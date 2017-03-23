# exploreHadoop

Use the following tutorial for Single Node Hadoop Cluster Setup on Ubuntu

http://www.michael-noll.com/tutorials/running-hadoop-on-ubuntu-linux-single-node-cluster/

## Java

`sudo apt-get install sun-java8-oracle`

## Add dedicated user

`sudo addgroup hadoop`

`sudo adduser --ingroup hadoop hduser`

`su - hduser`

`ssh-keygen -t rsa -P ""`

`cat $HOME/.ssh/id_rsa.pub >> $HOME/.ssh/authorized_keys`

## Hadoop

download and extract hadoop [http://www.apache.org/dyn/closer.cgi/hadoop/core]

`sudo chown -R hduser:hdgroup hadoop`

## Change bashrc

`export HADOOP_HOME=/usr/local/hadoop`

`export JAVA_HOME=/usr/lib/jvm/java-8-oracle`

## Edit *.xml (3-4)

### hadoop-env.sh

'export JAVA_HOME=/usr/lib/jvm/java-8-oracle'

### conf/*-site.xml

Refer tutorial to modify:
- core-site.xml
- mapred-site.xml
- hdfs-site.xml


## Node Bringup

`bin/hadoop namenode -format`

`bin/start-all.sh`

`bin/start-stop-all.sh`

## Overview

http://localhost:50070/dfshealth.html#tab-overview

http://localhost:8088/cluster

## References

http://www.michael-noll.com/tutorials/writing-an-hadoop-mapreduce-program-in-python/

http://blog.cloudera.com/blog/2013/01/a-guide-to-python-frameworks-for-hadoop/
