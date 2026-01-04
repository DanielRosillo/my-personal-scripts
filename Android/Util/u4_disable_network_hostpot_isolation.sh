# ROOT required
# Hospot Isolation
sudo iptables -I FORWARD -i wlan0 -o wlan0 -j ACCEPT
