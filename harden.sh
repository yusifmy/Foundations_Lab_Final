#!/bin/bash

# --- Secure the Local Vault ---
# Grant owner full access to the directory
chmod 700 ~/Vault
# Grant owner read/write access to the secret file
chmod 600 ~/Vault/secrets.txt

# --- Secure System Identity Files ---
# Apply the Gold Standard to /etc/shadow
sudo chmod 640 /etc/shadow
sudo chown root:shadow /etc/shadow

echo "Security hardening complete. Permissions restored."
