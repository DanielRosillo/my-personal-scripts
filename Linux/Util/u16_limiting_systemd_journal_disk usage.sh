– Acceder al SU
 	su
– Ejecutar:
	sudo nano /etc/systemd/journald.conf
– Configurar con la línea:
	SystemMaxUse=50M
sudo systemctl restart systemd-journald