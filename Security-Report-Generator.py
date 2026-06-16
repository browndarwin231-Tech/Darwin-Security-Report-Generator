incident = input("Enter incident: ")
severity = input("Enter severity (Low, Medium, High): ")

report = f"""
=== Security Report ===

Incident:
{incident}

Severity:
{severity}

Status:
Open

Analyst:
Darwin Brown
"""

print(report)

with open("security_report.txt", "w") as file:
    file.write(report)

print("Report saved successfully.")