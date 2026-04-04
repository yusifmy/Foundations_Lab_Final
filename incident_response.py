import subprocess
import json

# --- Phase 1: Log Interrogation ---
# Execute grep to find failed login attempts
result = subprocess.run(
    ["grep", "Failed password", "/var/log/titan_sim/auth_sim.log"],
    capture_output=True,
    text=True
)
raw_output = result.stdout

# --- Phase 2: Data Parsing ---
lines = raw_output.split('\n')
attacker_ips = []

for line in lines:
    if line:
        # Based on the log format, the IP address is at index 10
        parts = line.split(" ")
        if len(parts) > 10:
            ip = parts[10]
            attacker_ips.append(ip)

# --- Phase 3: The Export ---
alert_data = {
    "alert_type": "Brute Force",
    "attacker_ips": attacker_ips
}

# Write the structured JSON threat report
with open("threat_report.json", "w") as file:
    json.dump(alert_data, file, indent=4)

print("Mission Complete: threat_report.json has been generated.")
