#! /bin/bash
sudo nano /etc/sysctl.conf
#Agregar
net.ipv4.ip_forward = 1
sudo sysctl -p