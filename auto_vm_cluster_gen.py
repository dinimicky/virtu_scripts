import sys
from optparse import OptionParser
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
mip control boot-a_mip eth1:1 boot-a $BOOT_SERVER1$
mip control boot-b_mip eth1:2 boot-a $BOOT_SERVER2$

tipc all dynamic eth2
nfs $NFS_SERVER$
property control bootserver bootS
bootserver bootS servingblades 1 2 $PAYLOAD_LIST$
bootserver bootS mode backup
bootserver bootS network boot-a
#bootserver bootS network boot-b
bootserver bootS mip boot-a_mip
#bootserver bootS mip boot-b_mip

ssh.rootlogin all on

default-output vga

# End of file
'''
import re
PARAMETER_PATTERN = re.compile('\$([a-zA-Z0-9_]+)\$')

m = sys.modules[__name__]
print getattr(m, "cluster_conf")