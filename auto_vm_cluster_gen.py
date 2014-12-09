import sys
import importlib
cluster_conf = '''#
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
import re
PARAMETER_PATTERN = re.compile('\$([a-zA-Z0-9_]+)\$')

self_mod = sys.modules[__name__]

from optparse import OptionParser
def main():
    parser = OptionParser(usage="usage: %prog [options] filename",
                          version="%prog 1.0")
    parser.add_option("-m", "--macPrefix",
                      dest="startMac",
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
    (options, args) = parser.parse_args()

    if len(args) != 1:
        parser.error("wrong number of arguments")

    print options
    print args  
    

if __name__ == '__main__':
    main()