#!/bin/bash

function usage(){
    echo "The script is to start VM."
    echo ""
    echo "./vm_start.sh -m 2048 -v 1 -p 00:04:04:04 -i /home/ezonghu/mgc-sc-1.qcow -o /home/ezonghu/lde.iso"
    echo "-h help information"
    echo "-p the prefix of the mac address such as 00:04:04:04"
    echo "-i vm image such as /home/ezonghu/mgc-sc-1.qcow"
	echo "-o iso image such as /home/ezonghu/lde.iso"
	echo "-m the memory size such as 2048 means 2GB RAM"
	echo "-f the qemu-ifup script such as /etc/kvm/qemu-ifup"
	echo "-v the vnc id such as 1, it will be set in the 5th byte of the MAC address."
}

while getopts ":m:p:i:o:v:hf:" opt; do
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
			if [ $OPTARG -lt 100 ]; then
				VncId=$OPTARG
				MacId=`printf "%0.2d" $OPTARG`
			else
				echo "VncId must be less than 100"
				exit 1
			fi
			;;
		f)
			QemuIfup=$OPTARG
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

qemu-kvm \
-smp cpus=1,cores=2 -m 2048 -boot order=cdn  \
${Iso} \
${Image} \
-netdev type=tap,script=${QemuIfup},id=net${VncId}1 -device virtio-net-pci,netdev=net${VncId}1,mac=${MacPrefix}:${MacId}:00 \
-netdev type=tap,script=${QemuIfup},id=net${VncId}2 -device virtio-net-pci,netdev=net${VncId}2,mac=${MacPrefix}:${MacId}:01 \
-netdev type=tap,script=${QemuIfup},id=net${VncId}3 -device virtio-net-pci,netdev=net${VncId}3,mac=${MacPrefix}:${MacId}:02 \
-netdev type=tap,script=${QemuIfup},id=net${VncId}4 -device virtio-net-pci,netdev=net${VncId}4,mac=${MacPrefix}:${MacId}:03 \
-vnc :${VncId} -usb -usbdevice tablet &