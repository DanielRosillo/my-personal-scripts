# PARTICION FANTASMA
# Crear particion fantasma en una unidad de almacenamiento cualquiera.(Invisible en Windows)
# (solo debe estar conectado el disco sin montar ninguna particion)
# Notas: El espacio publico es accesible por cualquiera.
#----------------------CREACION UNIDAD---------------------
# Comandos:
sudo fdisk -l
sudo fdisk /dev/sdd
g
n
enter
enter
+{x}GB
# x = +cantidad de gb
#(REMOVE SIGNATURE=n)
n
enter
enter
enter
w
# Damos formato a la particion oculta puedes usar cualquier sistema de archivos.
sudo mkfs.ext4 /dev/sdd2
# Obtenemos la informacion del disco para ver los sectores y el tamaño
sudo fdisk -l /dev/sdd

# El inicio de la particion 2 se saca calculando el desplasamiento = IOsize*start(particion2)
# (solo debe estar conectado el disco sin montar ninguna particion)
# Montamos usando el desplazamiento (usar nombre d ela unidad general no 1,2,etc.)
sudo mount /dev/sdd /mnt/TEST -o offset=20000538624
# (ver si se monto correctamente)
df -Th
# EN ESTE PUNTO YA PODEMOS GUARDAR ARCHIVOS EN LA UNIDAD FANTASMA EN /mnt/TEST
# "DESTRUIR DISCO"
sudo fdisk /dev/sdd
g
w
# Formatear en NTFS con WINDOWS
#LA UNIDAD QUEDO LISTA AHORA WIDNOWS LA LEE COMO UNA UNIDAD VACIA NTFS PERO EN REALIDAD EN EL PUNTO DE MONTAJE 
# 21475885056 HAY UN SISTEMA DE ARCHIVOS CON EX4
#----------------------------DESMONTAR-------------------------------------
sudo umount /mnt/TEST
# SI NO SE DESMONTA
sudo fuser -k /mnt/TEST
#------------------------------MONTAR-------------------------------------------------
sudo mount /dev/sdd /mnt/TEST -o offset=20000538624
# en numero de desplazamiento es igual multiplicar el tamaño de la unidad de sector * unidad de comienzo
# sudo fdisk -l /dev/sdc