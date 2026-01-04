#! /bin/bash
sudo nano /etc/sysctl.conf
#Agregar
net.ipv4.icmp_echo_ignore_all = 1
sudo sysctl -p

