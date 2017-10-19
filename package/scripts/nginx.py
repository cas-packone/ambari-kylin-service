import os
import base64
from time import sleep
from resource_management import *

class NginxMaster(Script):
    nginx_packages = ['nginx']
    def install(self, env):      
        import params
        self.install_packages(env)
        if self.nginx_packages is not None and len(self.nginx_packages):
            for pack in self.nginx_packages:
                Package(pack) 
                

    def configure(self, env):  
        import params
        env.set_params(params)
        File(format("/etc/nginx/nginx.conf"), content=InlineTemplate(params.nginx_conf))
             
    def start(self, env):
        import params
        env.set_params(params)
        self.configure(env)
        Execute("service nginx start")
        

    def stop(self, env):
        Execute("nginx -s stop")


    def restart(self, env):
        Execute("nginx -s reload")

    def status(self, env):
        Execute("service nginx status")


if __name__ == "__main__":
    NginxMaster().execute()
