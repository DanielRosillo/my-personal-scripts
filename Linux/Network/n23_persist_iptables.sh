#! /bin/bash
#iptables -t nat -D POSTROUTING -s 10.8.0.0/24 -j SNAT --to XX.XXX.XX.XX
#iptables -t nat -A POSTROUTING -s 10.8.0.0/24 -o ens6 -j MASQUERADE
sudo apt install iptables-persistent
sudo netfilter-persistent save