#! /bin/bash
sudo apt update
sudo apt install openvpn
sudo mv cliente.ovpn /etc/openvpn/client/cliente.conf
sudo systemctl enable openvpn-client@cliente
sudo systemctl start openvpn-client@cliente