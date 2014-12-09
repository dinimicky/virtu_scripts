virtu_scripts
=============

> 1. auto_vm_cluster_gen to generate the cluster.conf and the qemu-kvm command to start the VMs

> + The minimum VMs is 2+2;
> + The max VMs is 2+10;
> + The each VM has 4 NICs;
>      + NIC 1 is for internal network
>      + NIC 2 is for boot-a network
>      + NIC 3 is for tipc
>      + NIC 4 is for evip fee
> + The NFS address will be in the last validate ip address in internal network
> + The Boot address will be in the last 2 validate ip addresses in boot network
> + The NFS & Boot address should be mip.
> + in cluster.conf, the default-output should be "vga".
> + The internal & boot-a ip address is from the last unused ip address.
> + input parameters:

>> 1.        -m : -startMac : start MAC address: "AB:cD:EF:GH"
>> 2.        -i : -intNet : internal subnet: "ww.xx.yy.zz/mm"
>> 3.        -b : -bootNet : boot-a subnet: "ww.xx.yy.zz/mm"
>> 4.        -p : -payload : payload number: xx from 2 to 10

> + output parameters:

>> 1. start_sc1_vm.sh : start SC-1 VM
>> 2. start_rest_vms.sh : start the rest VMs except SC-1
>> 3. auto_cluster.conf : cluster.conf file for virtual machines.