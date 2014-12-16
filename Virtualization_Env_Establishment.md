### Virtualization Environment Establishment


+ #### How to install the LDE on the VM

> **Note: in most situation, the SC-1 image has been ready, you needn't install a new one.**

> + create the SC-1 & SC-2 image:
`qemu-img create -f qcow2 $SC-IMG_NAME 50G`

>> For example: 
`qemu-img create -f qcow2 mgc-sc-1.qcow 50G`
`qemu-img create -f qcow2 mgc-sc-2.qcow 50G`

> Assume:

>> 
+ the path of the image: /home/ezonghu/mgc-sc-1.qcow
+ the path of the iso: /home/ezonghu/lde.iso
+ the path of the qemu-ifup script: /etc/kvm/qemu-ifup
+ the MAC prefix (the first 4 byte of the MAC address) of the VMs: 00:04:04:04
+ the VNC ID begin from 1
+ the Payload number is 4
+ SC blade memory is 2048MB
+ PL blade memeory is 4096MB

> + download the LDE ISO file

> + Dowload the [vm_start.sh](http://github.com/dinimicky/virtu_scripts/blob/master/vm_start.sh) script.

> + use the vm_start.sh to start a virtual machine. And then you can install it manually.

>> 
`./vm_start.sh -m 2048 -v 1 -p 00:04:04:04 -i /home/ezonghu/mgc-sc-1.qcow -o /home/ezonghu/lde.iso -f /etc/kvm/qemu-ifup`
**Note: you can use the vncviewer to do the following installation**
**Note: the default output should be 'vga'**

> + Download the [auto_vm_cluster_gen.py](http://github.com/dinimicky/virtu_scripts/blob/master/auto_vm_cluster_gen.py) script.

> + run the command to generate the cluster.conf file.

>> `./auto_vm_cluster_gen.py -b 192.168.88.16/28 -i 192.168.88.0/28 -m 00:04:04:04 -p 4`

> + update the cluster.conf in /cluster/etc/ and run the following commands:

>> ```
cluster rpm -a linux-control-R7B02-0.x86_64.rpm -n 2
cluster rpm -a linux-payload-R7B02-0.x86_64.rpm -n 3
cluster rpm -a linux-payload-R7B02-0.x86_64.rpm -n 4
cluster rpm -a linux-payload-R7B02-0.x86_64.rpm -n 5
cluster rpm -a linux-payload-R7B02-0.x86_64.rpm -n 6
cluster config -v
cluster config -r -a
cluster reboot -a
```

> + start the rest VMs

>> ```
./vm_start.sh -m 2048 -v 2 -p 00:04:04:04 -i /home/ezonghu/mgc-sc-2.qcow -f /etc/kvm/qemu-ifup
./vm_start.sh -m 4096 -v 3 -p 00:04:04:04 -f /etc/kvm/qemu-ifup
./vm_start.sh -m 4096 -v 4 -p 00:04:04:04 -f /etc/kvm/qemu-ifup
./vm_start.sh -m 4096 -v 5 -p 00:04:04:04 -f /etc/kvm/qemu-ifup
./vm_start.sh -m 4096 -v 6 -p 00:04:04:04 -f /etc/kvm/qemu-ifup
```

+ #### How to install the MGC

> + Install ait component on the SC-1

> + Prepare the DEPLOYMENT.READY file

> + Prepare a correct repository


