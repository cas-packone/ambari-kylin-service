from resource_management import *
from resource_management.libraries.script.script import Script

# server configurations
config = Script.get_config()
install_dir = config['configurations']['kylin']['install.dir']
