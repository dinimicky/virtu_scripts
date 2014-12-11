### Virtualization Environment Establishment


+ #### How to install the SC-1 by LDE iso file

> **Note: in most situation, the SC-1 image has been ready, you needn't install a new one.**

> + download the LDE ISO file

> + use the qemu-kvm to start a virtual machine. And then you can install it manually.

>> ```
#SC-1
qemu-kvm \
-smp cpus=1,cores=2 -m 2048 -boot order=cd  -cdrom /home/ezonghu/lde.iso \
-drive file=/home/ezonghu/mgc-sc-1.qcow,if=virtio,media=disk \
-netdev type=tap,script=/etc/kvm/qemu-ifup,id=net2 \
-device virtio-net-pci,netdev=net2,mac=00:04:04:04:00:00 \
-netdev type=tap,script=/etc/kvm/qemu-ifup,id=net3 \
-device virtio-net-pci,netdev=net3,mac=00:04:04:04:00:01 \
-netdev type=tap,script=/etc/kvm/qemu-ifup,id=net4 \
-device virtio-net-pci,netdev=net4,mac=00:04:04:04:00:02 \
-netdev type=tap,script=/etc/kvm/qemu-ifup,id=net5 \
-device virtio-net-pci,netdev=net5,mac=00:04:04:04:00:03 \
-vnc :1 -usb -usbdevice tablet &
```

> + update the cluster.conf in /cluster/etc/

> ```
cluster config -v
cluster config -r -a
cluster reboot -a
```

> + use the qemu-kvm to start the rest virtual machines.

>> ```
#SC-2
qemu-kvm \
-smp cpus=1,cores=2 -m 2048 -boot order=cn  \
-drive file=/home/ezonghu/mgc-sc-2.qcow,if=virtio,media=disk \
-netdev type=tap,script=/etc/kvm/qemu-ifup,id=net12 \
-device virtio-net-pci,netdev=net12,mac=00:04:04:04:01:00 \
-netdev type=tap,script=/etc/kvm/qemu-ifup,id=net13 \
-device virtio-net-pci,netdev=net13,mac=00:04:04:04:01:01 \
-netdev type=tap,script=/etc/kvm/qemu-ifup,id=net14 \
-device virtio-net-pci,netdev=net14,mac=00:04:04:04:01:02 \
-netdev type=tap,script=/etc/kvm/qemu-ifup,id=net15 \
-device virtio-net-pci,netdev=net15,mac=00:04:04:04:01:03 \
-vnc :2 -usb -usbdevice tablet &
```
```
#PL-3
qemu-kvm \
-smp cpus=1,cores=2 -m 4096 -boot n  \
-netdev type=tap,script=/etc/kvm/qemu-ifup,id=net22 \
-device virtio-net-pci,netdev=net22,mac=00:04:04:04:02:00 \
-netdev type=tap,script=/etc/kvm/qemu-ifup,id=net23 \
-device virtio-net-pci,netdev=net23,mac=00:04:04:04:02:01 \
-netdev type=tap,script=/etc/kvm/qemu-ifup,id=net24 \
-device virtio-net-pci,netdev=net24,mac=00:04:04:04:02:02 \
-netdev type=tap,script=/etc/kvm/qemu-ifup,id=net25 \
-device virtio-net-pci,netdev=net25,mac=00:04:04:04:02:03 \
-vnc :3 -usb -usbdevice tablet &
```
```
#PL-4
qemu-kvm \
-smp cpus=1,cores=2 -m 4096 -boot n  \
-netdev type=tap,script=/etc/kvm/qemu-ifup,id=net32 \
-device virtio-net-pci,netdev=net32,mac=00:04:04:04:03:00 \
-netdev type=tap,script=/etc/kvm/qemu-ifup,id=net33 \
-device virtio-net-pci,netdev=net33,mac=00:04:04:04:03:01 \
-netdev type=tap,script=/etc/kvm/qemu-ifup,id=net34 \
-device virtio-net-pci,netdev=net34,mac=00:04:04:04:03:02 \
-netdev type=tap,script=/etc/kvm/qemu-ifup,id=net35 \
-device virtio-net-pci,netdev=net35,mac=00:04:04:04:03:03 \
-vnc :4 -usb -usbdevice tablet &
```
```
#PL-5
qemu-kvm \
-smp cpus=1,cores=2 -m 4096 -boot n  \
-netdev type=tap,script=/etc/kvm/qemu-ifup,id=net42 \
-device virtio-net-pci,netdev=net42,mac=00:04:04:04:04:00 \
-netdev type=tap,script=/etc/kvm/qemu-ifup,id=net43 \
-device virtio-net-pci,netdev=net43,mac=00:04:04:04:04:01 \
-netdev type=tap,script=/etc/kvm/qemu-ifup,id=net44 \
-device virtio-net-pci,netdev=net44,mac=00:04:04:04:04:02 \
-netdev type=tap,script=/etc/kvm/qemu-ifup,id=net45 \
-device virtio-net-pci,netdev=net45,mac=00:04:04:04:04:03 \
-vnc :5 -usb -usbdevice tablet &
```
```
#PL-6
qemu-kvm \
-smp cpus=1,cores=2 -m 4096 -boot n  \
-netdev type=tap,script=/etc/kvm/qemu-ifup,id=net52 \
-device virtio-net-pci,netdev=net52,mac=00:04:04:04:05:00 \
-netdev type=tap,script=/etc/kvm/qemu-ifup,id=net53 \
-device virtio-net-pci,netdev=net53,mac=00:04:04:04:05:01 \
-netdev type=tap,script=/etc/kvm/qemu-ifup,id=net54 \
-device virtio-net-pci,netdev=net54,mac=00:04:04:04:05:02 \
-netdev type=tap,script=/etc/kvm/qemu-ifup,id=net55 \
-device virtio-net-pci,netdev=net55,mac=00:04:04:04:05:03 \
-vnc :6 -usb -usbdevice tablet &
```

