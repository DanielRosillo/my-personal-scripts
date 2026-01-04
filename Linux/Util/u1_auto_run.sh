#! /bin/bash
# CREAR SERVICIO PROPIO DE EJECUCION DE SCRIPTS
# Agregar codigo a /bin/autoexec
sudo cat > /bin/autoexec << EOF
    #! /bin/bash
EOF

 #! /bin/bash
        sudo cat > /usr/lib/systemd/system/autoexec.service << EOF
        [Unit]
        Description = Autoexec
        [Service]
        Type = oneshot
        ExecStart=/bin/bash /bin/autoexec
        RemainAfterExit=yes
        [Install]
        WantedBy = multi-user.target
EOF

sudo systemctl enable autoexec
sudo chmod +x /bin/autoexec