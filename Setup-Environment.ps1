Install-BoxstarterPackage -PackageName https://raw.githubusercontent.com/Infekma/Boxstarter-Test/main/Latest.txt -DisableReboots

# START - setup boost

# download the boost setup python script
$fileUrl = 'https://raw.githubusercontent.com/Infekma/Boxstarter-Test/main/Test/setup-boost.py'
$output = "$PSScriptRoot\setup-boost.py"
(New-Object System.Net.WebClient).DownloadFile($fileUrl, $output)

# run the boost setup script and then delete it afterwards
python $output
Remove-Item($output)

# END - setup boost
