#!/bin/bash

function usage(){
    echo "The script is to start VM."
    echo ""
    echo "./vm_start.sh -m 2048 -v 1 -p 00:04:04:04 -i /home/ezonghu/mgc-sc-1.qcow -o /home/ezonghu/lde.iso"
    echo "-h --help"
    echo "-p the prefix of the mac address such as 00:04:04:04"
    echo "-i vm image such as /home/ezonghu/mgc-sc-1.qcow"
	echo "-o iso image such as /home/ezonghu/lde.iso"
	echo "-m the memory size such as 2048 means 2GB RAM"
	echo "-v the vnc id such as 1, it will be set in the 5th byte of the MAC address."
}

while getopts ":m:p:i:o:v:h:" opt; do
    case $opt in
	    m)
		    Mem=$OPTARG
		    ;;
		p)
		    MacPrefix=$OPTARG
			;;
		i)
		    Image="-drive file="$OPTARG",if=virtio,media=disk "
			;;
		o)
		    Iso="-cdrom "$OPTARG" "
			;;
		v)
		    VncId=$OPTARG
			;;
		h)
		    usage
			exit
			;;
		\?)
		    usage
			exit 1
			;;
	esac
		
done

echo $Mem $MacPrefix $Image $Iso $VncId
"
qemu-kvm \
-smp cpus=1,cores=2 -m 2048 -boot order=cd  -cdrom /home/ezonghu/lde.iso \
-drive file=/home/ezonghu/mgc-sc-1.qcow,if=virtio,media=disk \
-netdev type=tap,script=/etc/kvm/qemu-ifup,id=net2 -device virtio-net-pci,netdev=net2,mac=00:04:04:04:00:00 \
-netdev type=tap,script=/etc/kvm/qemu-ifup,id=net3 -device virtio-net-pci,netdev=net3,mac=00:04:04:04:00:01 \
-netdev type=tap,script=/etc/kvm/qemu-ifup,id=net4 -device virtio-net-pci,netdev=net4,mac=00:04:04:04:00:02 \
-netdev type=tap,script=/etc/kvm/qemu-ifup,id=net5 -device virtio-net-pci,netdev=net5,mac=00:04:04:04:00:03 \
-vnc :1 -usb -usbdevice tablet &"