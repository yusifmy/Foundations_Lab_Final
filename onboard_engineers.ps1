# ==================================================
# SESSION 13: THE AUTOMATED ONBOARDING
# Operator Deployment Script
# ==================================================

Write-Host "[*] Beginning Engineering Onboarding..."

for ($i=1; $i -le 5; $i++) {
    New-ADUser -Name "Eng_User$i" -Path "OU=Engineering,DC=titan,DC=local" -ChangePasswordAtLogon $true -Enabled $true
}

Write-Host "[+] All engineers onboarded successfully."
