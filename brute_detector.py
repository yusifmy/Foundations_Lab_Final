# Step 2: Initialize the Counter
attack_count = 0

# Step 3 & 4: The Double-Door Logic (Open source to read, report to write)
try:
    with open("auth_audit.log", "r") as log_file:
        with open("brute_report.txt", "w") as report_file:
            
            # Step 5: The Loop (The Conveyor Belt)
            for line in log_file:
                
                # Step 6: The Signature Search (Case Sensitive!)
                if "Failed password" in line:
                    
                    # Step 7: Save to the report and increment counter
                    report_file.write(line)
                    attack_count += 1

    # Step 8: The Final Report (Flush to the left, outside the 'with' block)
    print(f"[*] Audit Complete. Extracted {attack_count} threat signatures to brute_report.txt")

except FileNotFoundError:
    print("[-] Error: 'auth_audit.log' not found. Please ensure the log exists.")
