#! /bin/bash
# n5_internet_foward
# to delete -> -D
sudo iptables -t nat -A PREROUTING -i ens6 -p tcp --dport 5000 -j DNAT --to-destination 10.8.0.223:5000
sudo iptables -t nat -A POSTROUTING -o tun0 -p tcp -d 10.8.0.223 --dport 5000 -j MASQUERADE