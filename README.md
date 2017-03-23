#Hadoop 101

Use the following tutorial for Single Node Hadoop Cluster Setup on Ubuntu

http://www.michael-noll.com/tutorials/running-hadoop-on-ubuntu-linux-single-node-cluster/

### Java

`sudo apt-get install sun-java8-oracle`

### Add dedicated user

`sudo addgroup hadoop`

`sudo adduser --ingroup hadoop hduser`

`su - hduser`

`ssh-keygen -t rsa -P ""`

`cat $HOME/.ssh/id_rsa.pub >> $HOME/.ssh/authorized_keys`

### Hadoop Setup

download and extract hadoop [http://www.apache.org/dyn/closer.cgi/hadoop/core]

`sudo chown -R hduser:hdgroup hadoop`

### Change bashrc

`export HADOOP_HOME=/usr/local/hadoop`

`export JAVA_HOME=/usr/lib/jvm/java-8-oracle`

### Edit Config Files

#### hadoop-env.sh

'export JAVA_HOME=/usr/lib/jvm/java-8-oracle'

#### conf/*-site.xml

Refer tutorial to modify:
- core-site.xml
- mapred-site.xml
- hdfs-site.xml


### Node Bringup

`bin/hadoop namenode -format`

`bin/start-all.sh`

`bin/start-stop-all.sh`

### Overview

http://localhost:50070/dfshealth.html#tab-overview

http://localhost:8088/cluster

### References

http://www.michael-noll.com/tutorials/writing-an-hadoop-mapreduce-program-in-python/

http://blog.cloudera.com/blog/2013/01/a-guide-to-python-frameworks-for-hadoop/

## MapReduce

### Create input file, mapper and reducer

eg any text file for now

mapper and reducer split task

check using - `cat data | map | sort | reduce`

### Move file to hdfs

- user to hd - `sudo cp /home/USER1/FNAME /home/USER2/FNAME && sudo chown USER2:USER2 /home/USER2/FNAME`
- make hdfs directory - `hdfs dfs -mkdir /input`
- hduser to hdfs- `bin/hadoop fs -put *.txt /tmp/In`

### Run Task

`hadoop jar /usr/local/hadoop/share/hadoop/tools/lib/hadoop-streaming-2.7.3.jar -input /tmp/In/*.txt -output /tmp/In/output -mapper /home/hduser/mapper.py -reducer /home/hduser/reducer.py`

### Output

`bin/hadoop fs -get /tmp/In/out /home/hduser/`

OR

`bin/hadoop dfs -cat /tmp/In/out/part-00000`
