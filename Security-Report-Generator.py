failed_logins = 0
phishing_urls = 0
ioc_count = 0
file_modified = False

print("=== Darwin Security Report Generator ===\n")

with open("security_events.txt", "r") as file:
    events = file.readlines()

for event in events:
    event = event.strip()

    if event == "FAILED_LOGIN":
        failed_logins += 1

    elif event == "PHISHING_URL":
        phishing_urls += 1

    elif event == "IOC_FOUND":
        ioc_count += 1

    elif event == "FILE_MODIFIED":
        file_modified = True

print("========== INCIDENT REPORT ==========\n")

print(f"Failed Login Attempts : {failed_logins}")
print(f"Phishing URLs Found  : {phishing_urls}")
print(f"IOCs Detected         : {ioc_count}")

if file_modified:
    print("File Integrity        : MODIFIED")
else:
    print("File Integrity        : CLEAN")

print()

if failed_logins >= 3 or phishing_urls >= 2 or file_modified:
    print("Overall Risk Level : HIGH")
    print("\nRecommendations:")
    print("- Investigate affected accounts")
    print("- Block malicious URLs")
    print("- Review endpoint logs")
    print("- Restore modified files if necessary")
else:
    print("Overall Risk Level : LOW")
