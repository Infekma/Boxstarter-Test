# save and restore the execution policy after we finish
$prevExecPolicy = Get-ExecutionPolicy
Set-ExecutionPolicy Unrestricted -Force
$WebClient = New-Object System.Net.WebClient
iex ($WebClient.DownloadString('https://boxstarter.org/bootstrapper.ps1')); Get-Boxstarter -Force

# start the box starter shell
BOXSTARTERSHELL 
iex ($WebClient.DownloadString('https://github.com/Infekma/Boxstarter-Test/blob/main/Setup-Environment.ps1'));

# recover the old execution policy
Set-ExecutionPolicy $prevExecPolicy -Force
