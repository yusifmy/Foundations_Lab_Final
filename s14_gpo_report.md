# S14 Provisioning: GPO Audit Artifact Seeding
$TargetDir = "C:\Users\Administrator\Desktop"
$ArtifactPath = "$TargetDir\gpo_audit.txt"

Write-Host "[*] Initializing Session 14 Environment..." -ForegroundColor Cyan

$Template = @"
==================================================
SESSION 14: GROUP POLICY AUDIT REPORT
==================================================

QUESTION 1: What specific command do you run on a client machine to force it to download the latest Group Policy from the Domain Controller?
ANSWER: The gpupdate /force command tells the Windows OS to immediately pull and apply all Group Policy settings from the Domain Controller. It was necessary because GPOs usually only refresh every 90 minutes; without this command, our Lockdown_ControlPanel restriction wouldn't have taken effect immediately to block the engineering team.

QUESTION 2: Explain the LSDOU acronym. If a Local Policy says "Enable USB" but the Domain Policy says "Disable USB", which one wins and why?
ANSWER: LSDOU stands for Local, Site, Domain, and Organizational Unit (OU). This is the chronological order in which Windows applies Group Policies. Policies are applied starting with the Local machine, then the Active Directory Site, then the Domain, and finally the specific OU where the user or computer is located.

QUESTION 3: Why is it best practice to apply GPOs to Organizational Units (OUs) rather than the entire Domain?
ANSWER: he OU-level GPO wins. This is because of the "Last Writer Wins" rule in the LSDOU model. Since the OU policy is applied last, it overrides any conflicting settings that were applied earlier at the Site or Domain levels. This allows us to have specific restrictions for the Engineering team that might not apply to the rest of the company.
"@

Set-Content -Path $ArtifactPath -Value $Template
Write-Host "[+] PROVISIONING COMPLETE. Artifact template seeded at: $ArtifactPath" -ForegroundColor Green
