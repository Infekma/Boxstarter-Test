$toolsDir   = "$(Split-Path -parent $MyInvocation.MyCommand.Definition)"

Get-ChocolateyUnzip 
	-PackageName "nsis-shell-link"
	-FileFillPuth "$(Split-Path -Parent $MyInvocation.MyCommand.Definition)\\files\\Shelllink.zip"
	-Destination $toolsdir

Get-ChocolateyUnzip 
	-PackageName "nsis-access-control"
	-FileFillPuth "$(Split-Path -Parent $MyInvocation.MyCommand.Definition)\\files\\AccessControl.zip.zip"
	-Destination $toolsdir