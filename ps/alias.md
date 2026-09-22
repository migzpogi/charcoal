### Locate PowerShell Profile
```
PS> echo $profile

C:\Users\...\WindowsPowerShell\Microsoft.PowerShell_profile.ps1
```
If it doesn't exists, create the directory and or file. If it does, then open `Microsoft.PowerShell_profile.ps1` to edit it.

### Aliases
```
Set-Alias -Name aliasname -Value Get-Location
Set-Alias -Name activate -Value "C:\venv\Scripts\Activate.ps1"
```
We set an alias by using `Set-Alias -Name` then its corresponding action by `-Value`. PowerShell scripts can be linked as well. This is actually a good practice to prevent cluttering your profile file.

### Display Your Profile Alias
I like to create an alias to display all of my aliases. First, create a .PS1 file in your profile directory. Let's name it: `C:\Users\...\WindowsPowerShell\myalias.ps1`
```
Select-String -Path $PROFILE -Pattern '(?<=\b(Set|New)-Alias -Name\s+)\w+' | ForEach-Object { Get-Alias $_.Matches.Value -ErrorAction SilentlyContinue } | Select-Object Name, Definition | Format-Table -Wrap
```
Then edit `C:\Users\...\WindowsPowerShell\PowerShell_profile.ps1`
```
Set-Alias -Name aliasname -Value Get-Location
Set-Alias -Name activate -Value "C:\venv\Scripts\Activate.ps1"
Set-Alias -Name myalias -Value "C:\Users\...\WindowsPowerShell\myalias.ps1"
```
Close all open terminals and create a new PowerShell session.
```
PS> myalias

Name    Definition                                                                    
----    ----------                                                                    
myalias C:\Users\...\myalias.ps1                  
venvbc  C:\Users\...\Activate.ps1
kk      Get-Location   
```