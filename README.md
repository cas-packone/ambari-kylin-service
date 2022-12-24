ambari-kylin-service
===

## To download the Kylin service folder, run below    

```
VERSION=`hdp-select status hadoop-client | sed 's/hadoop-client - \([0-9]\.[0-9]\).*/\1/'`
sudo git clone https://github.com/cas-bigdatalab/ambari-kylin-service.git /var/lib/ambari-server/resources/stacks/HDP/$VERSION/services/KYLIN
```
## Restart Ambari
\#sandbox  
service ambari restart

\#non sandbox  
sudo service ambari-server restart

At the install process, when setting the configuration, set the value for `download.location` with the path to the package `apache-kylin.tar` in one of the  [releases](https://github.com/cas-packone/ambari-kylin-service/releases).

## SUMMARY
![Image](../master/screenshots/kylin.png?raw=true)
