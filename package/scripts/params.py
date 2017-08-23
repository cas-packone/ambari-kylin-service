from resource_management import *
from resource_management.libraries.script.script import Script
import sys, os, glob,socket

# server configurations
config = Script.get_config()
service_packagedir = os.path.realpath(__file__).split('/scripts')[0]
tmp_dir = Script.get_tmp_dir()
kylin_properties=config['configurations']['kylin']['kylin_properties']
hdp_version =  default("/commandParams/version", None)
downloadlocation = config['configurations']['kylin']['download.location']
#install_dir = config['configurations']['kylin']['install.dir']
install_dir = format('/usr/hdp/{hdp_version}/kylin')
current_host_name = socket.gethostname()
server_mode = "query"
server_masters = config['clusterHostInfo']['kylin_all_hosts'][0]
server_clusters_arr = config['clusterHostInfo']['kylin_all_hosts'] + config['clusterHostInfo']['kylin_query_hosts']
server_port = "7070"
server_clusters = ','.join(i+":" + server_port for i in server_clusters_arr)
hadoop_conf_dir = install_dir + "/latest/conf/hadoop_conf"
