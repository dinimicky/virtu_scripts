import ipcalc

class Config(object):
    import re
    Parameter_Pattern = re.compile('\$([a-zA-Z0-9_]+)\$')
    Config_Template = ""
    @classmethod
    def get_parameter_names(cls):
        return [c.group(1) for c in cls.Parameter_Pattern.finditer(cls.Config_Template)]
    
    @classmethod
    def get_config_source(cls):
        return cls.Parameter_Pattern.sub('%s', cls.Config_Template)
     
class Cluster(Config):
    def __init__(self, macPrefix="00:04:04:04", 
                 intNet="192.168.88.0/28", 
                 bootNet="192.168.88.16/28", 
                 payload=2):
        self.macPrefix = macPrefix
        self.intNet = intNet
        self.intIPs = [str(ip) for ip in ipcalc.Network(self.intNet)]
        self.bootNet = bootNet
        self.bootIPs = [str(ip) for ip in ipcalc.Network(self.bootNet)]
        self.payload = payload
        self.vNICs = 4
        self.SCs = 2
        self.config_parameters = self.get_parameter_names()
        self.config_source = self.get_config_source()
        
    def gen_cluster_conf(self):
        Parameters = [ getattr(self, "get_%s" % name)() for name in self.config_parameters]
        return self.config_source % tuple(Parameters)        
    
    def get_NODE_LIST(self):
        Node_List = []
        Control_Node = "node %d control SC-%d"
        Node_List.extend([Control_Node % (i+1, i+1) for i in range(self.SCs)])
        Payload_Node = "node %d payload PL-%d"
        Node_List.extend([Payload_Node % (i+3, i+3) for i in range(self.payload)])
        return "\n".join(Node_List)
    
    def get_MAC_INTF_LIST(self):
        Mac_Lists = []
        Mac = "interface %d eth%d ethernet %s:%0.2d:%0.2d"
        for i in range(1, self.SCs+self.payload+1):
            for j in range(self.vNICs):
                Mac_Lists.append(Mac % (i, j, self.macPrefix, i, j))
                
        return "\n".join(Mac_Lists)
    
    def get_intNet(self):
        return self.intNet
    
    def get_bootNet(self):
        return self.bootNet
    
    def get_NFS_SERVER(self):
        return self.intIPs[-1]
    
    def get_BOOT_SERVER(self):
        return self.bootIPs[-1]
    
    def get_INT_IP_LIST(self):
        INT_IP = "ip %d eth0 internal %s"
        INT_IP_LIST = [INT_IP % (i, self.intIPs[i*(-1)-1]) for i in range(1, self.SCs+self.payload+1)]
        return "\n".join(INT_IP_LIST)
        
    def get_BOOT_IP_LIST(self):
        BOOT_IP = "ip %d eth1 boot-a %s"
        BOOT_IP_LIST = [BOOT_IP % (i, self.bootIPs[i*(-1)-1])for i in range(1, self.SCs+self.payload+1)]
        return "\n".join(BOOT_IP_LIST)
                
    Config_Template = '''#
# Default cluster.conf, generated Mon Jan  1 00:00:11 UTC 2007
#
# For information about the file format, see the LDE User Guide
#

timezone Asia/Beijing

# Define nodes. Id, type and name are fixed.

$NODE_LIST$

#Define node interfaces
$MAC_INTF_LIST$

network internal $intNet$
network boot-a $bootNet$

interface control eth0:1 alias
interface control eth1:1 alias
interface control eth1:2 alias

$INT_IP_LIST$

$BOOT_IP_LIST$

mip control nfs eth0:1 internal $NFS_SERVER$
mip control boot-a_mip eth1:1 boot-a $BOOT_SERVER$

tipc all dynamic eth2
nfs $NFS_SERVER$
property control bootserver bootS
bootserver bootS servingblades all
bootserver bootS mode backup
bootserver bootS network boot-a
bootserver bootS mip boot-a_mip

ssh.rootlogin all on

default-output vga

# End of file
'''

from optparse import OptionParser
def parse_parameters():
    parser = OptionParser(usage="usage: %prog [options] filename",
                          version="%prog 1.0")
    parser.add_option("-m", "--macPrefix",
                      dest="macPrefix",
                      help='MAC address Prefix: AB:cD:EF:GH')
    parser.add_option("-i", "--intNet",
                      dest="intNet",
                      help='internal subnet: ww.xx.yy.zz/mm')
    parser.add_option("-b", "--bootNet",
                      dest="bootNet",
                      help='boot-a subnet: ww.xx.yy.zz/mm')
    parser.add_option("-p", "--payload",
                      type = 'int',
                      dest="payload",
                      help='payload number: xx from 2 to 10')        
    (options, _args) = parser.parse_args()
    
    for opt, value in options.__dict__.items():
        if value is None:
            parser.error("Missing Required parameters: %s" % opt)
    return options


def main():
    config_info = parse_parameters()
    print(Cluster(**config_info.__dict__).gen_cluster_conf())

if __name__ == '__main__':
    main()