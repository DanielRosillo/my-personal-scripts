#! /bin/bash
sudo apt-get install vsftpd -y
sudo rm /etc/vsftpd.conf
sudo nano /etc/vsftpd.conf
systemctl restart vsftpd
sudo chown charlie:charlie /home/charlie/dc-root
