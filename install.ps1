$url = "github.com/MIKTHATGUY/Flow/releases/latest/download/EasyFlog.exe"
# Destation file
$dest = ".\EasyFlog.exe"
# Download the file
Invoke-WebRequest -Uri $url -OutFile $dest

Move-Item -Path $dest -Destination c:\windows\system32 -force
echo %WINDIR%\system32