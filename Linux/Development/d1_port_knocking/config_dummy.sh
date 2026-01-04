sudo modprobe -v dummy numdummies=1
sudo ip link set up dummy0
sudo ip add add 10.10.10.1/32 dev dummy0