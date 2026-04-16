# TITAN SMALL BUSINESS SERVICES: SECURITY ARCHITECTURE DOCUMENT (SAD)
**Operator:** Muhammed Yusif
**Date:** 04/15/2026

## 1. Perimeter Hardening (UFW & SSH)
* **SSH Status:** Changed PermitRootLogin to no and PasswordAuthentication to no in /etc/ssh/sshd_config.
* **Firewall Logic:** Set default deny for incoming traffic. Explicitly allowed port 22/tcp for management and 8080/tcp for the application.

## 2. The Automated Auditor (Python)
* **Script Logic:** 
import os
hostname = "10.0.2.15"
response = os.system(f"ping -c 4 {hostname}")
with open("/var/log/dc_audit.log", "a") as log:
    if response == 0:
        log.write("DC is UP\n")
    else:
        log.write("DC is DOWN\n")
* **Telemetry Path:** ~/dc_auditor.py (logging to /var/log/dc_audit.log).`

## 3. Containerized App (Docker)
* **Network Isolation:** Deployed two networks: frontend and backend. The database (db) is placed exclusively on the backend network with internal: true to prevent external access.
* **Stack Health:** NAME                IMAGE     COMMAND                  SERVICE   STATUS           PORTS
muhammed-yusif-db-1   mysql     "docker-entrypoint.s…"   db        Up 12 minutes    3306/tcp, 33060/tcp
muhammed-yusif-wiki-1  nginx     "/docker-entrypoint.…"   wiki      Up 12 minutes    0.0.0.0:8080->80/tcp 

## 4. Executive Summary
The Hardened Outpost is secured using a defense-in-depth approach. Perimeter security is maintained through hardened SSH configurations and a restrictive UFW firewall. Continuous monitoring is automated via a custom Python auditing script, while the application architecture utilizes segmented Docker networks to ensure the database remains internally isolated and air-gapped from external threats.

