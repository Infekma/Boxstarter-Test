Install-BoxstarterPackage -PackageName https://raw.githubusercontent.com/Infekma/Boxstarter-Test/main/Latest.txt -DisableReboots

# download the boost setup python script
$fileUrl = 'https://raw.githubusercontent.com/Infekma/Boxstarter-Test/main/Boost/main_setup_boost.py'
$output = "$PSScriptRoot\main_setup_boost.py"
(New-Object System.Net.WebClient).DownloadFile($fileUrl, $output)

# run the boost setup script and then delete it afterwards
python $output
Remove-Item($output)

# END - setup boost
