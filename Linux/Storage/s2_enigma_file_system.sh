#!/bin/bash
# Unidad con cifrado de grado militar
# ---------------------------CREAR------------------------
sudo dd if=/dev/zero of=backup.rosillo bs=1G count=5
sudo cryptsetup -v --cipher aes-xts-plain64 --key-size 512 --hash sha512 --iter-time 5000 --use-random luksFormat --type luks2 backup.rosillo
sudo cryptsetup open --type luks2 backup.rosillo BACKUPCLOUD
sudo mkfs.ext4 /dev/mapper/BACKUPCLOUD
# ---------------------ABRIR------------------------------
sudo cryptsetup open --type luks2 backup.rosillo BACKUPCLOUD
sudo mount /dev/mapper/BACKUPCLOUD /mnt/BACKUPCLOUD
# ---------------------CERRAR-----------------------------
sudo umount /dev/mapper/BACKUPCLOUD
sudo cryptsetup luksClose BACKUPCLOUD

sudo lsof /mnt/BACKUPCLOUD