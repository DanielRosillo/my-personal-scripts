#!/bin/bash
sudo apt install build-essential
sudo apt install firmware-brcm80211
sudo apt install network-manager
sudo apt install wpasupplicant

sudo bash -c 'cat > /etc/wpa_supplicant/wpa_supplicant.conf <<EOF
network={
    ssid="NOMBRE_DE_TU_WIFI"
    psk="CONTRASEÑA_DE_TU_WIFI"
}
EOF'

sudo ip link set wlan0 up
rfkill list all
sudo rfkill unblock wifi
sudo wpa_supplicant -B -i wlan0 -c /etc/wpa_supplicant/wpa_supplicant.conf
sudo dhclient wlan0