from datetime import datetime
import uuid

# Client & Case Creation
def create_case():
    print("\n--- New Support Case ---")
    name = input("Client Name: ")
    email = input("Client Email: ")

    case_id = str(uuid.uuid4())[:8]
    created_time = datetime.now()

    return {
        "case_id": case_id,
        "name": name,
        "email": email,
        "created_time": created_time
    }

# Issue Categories
def show_issues():
    print("\nIssue Categories:")
    print("1. Network Issue")
    print("2. Application Issue")
    print("3. System Performance Issue")
    print("4. Security / Access Issue")
    print("5. Search Previous Case")
    print("6. Exit")

def network_issue():
    wifi = input("Is the device connected to a network? (yes/no): ").lower()
    if wifi == "no":
        return "No network connection", "Ask user to connect to Wi-Fi or LAN", "P2"

    access = input("Can internal sites be accessed? (yes/no): ").lower()
    if access == "no":
        return "DNS or internal routing issue", "Flush DNS / escalate to network team", "P1"

    return "Intermittent connectivity", "Restart network adapter", "P3"

# Application Issues
def application_issue():
    error = input("Does the application show an error message? (yes/no): ").lower()
    if error == "yes":
        return "Application crash or dependency failure", "Reinstall / update application", "P2"

    return "Permission or configuration issue", "Run as admin / check configs", "P3"

# System Performance
def performance_issue():
    cpu = input("Is system slow even when idle? (yes/no): ").lower()
    if cpu == "yes":
        return "High background resource usage", "Disable startup apps / scan malware", "P2"

    return "Temporary performance degradation", "Restart system", "P4"

# Security / Access Issue
def security_issue():
    access = input("Is the user unable to login? (yes/no): ").lower()
    if access == "yes":
        return "Authentication or account lock issue", "Reset password / unlock account", "P1"

    return "Permission misconfiguration", "Verify user roles and access rights", "P2"

# Case Logging
def log_case(case, issue, diagnosis, solution, priority):
    with open("cases.log", "a") as log:
        log.write(
            f"{datetime.now()} | CaseID: {case['case_id']} | "
            f"Client: {case['name']} | Issue: {issue} | "
            f"Diagnosis: {diagnosis} | Priority: {priority}\n"
        )

    with open("case_history.txt", "a") as history:
        history.write(
            f"\nCase ID: {case['case_id']}\n"
            f"Client: {case['name']} ({case['email']})\n"
            f"Issue: {issue}\n"
            f"Diagnosis: {diagnosis}\n"
            f"Solution: {solution}\n"
            f"Priority: {priority}\n"
            f"Created: {case['created_time']}\n"
            + "-"*40
        )

# Search Previous Cases
def search_case():
    case_id = input("Enter Case ID to search: ")
    with open("case_history.txt", "r") as history:
        data = history.read()

        if case_id in data:
            print("\n--- Case Found ---")
            print(data.split(case_id)[1].split("-"*40)[0])
        else:
            print("Case not found.")

def main():
    while True:
        show_issues()
        choice = input("\nSelect option: ")

        if choice in ["1", "2", "3", "4"]:
            case = create_case()

            if choice == "1":
                diagnosis, solution, priority = network_issue()
                issue = "Network Issue"

            elif choice == "2":
                diagnosis, solution, priority = application_issue()
                issue = "Application Issue"

            elif choice == "3":
                diagnosis, solution, priority = performance_issue()
                issue = "Performance Issue"

            elif choice == "4":
                diagnosis, solution, priority = security_issue()
                issue = "Security / Access Issue"

            print(f"\nDiagnosis: {diagnosis}")
            print(f"Solution: {solution}")
            print(f"Priority: {priority}")

            log_case(case, issue, diagnosis, solution, priority)
            print(f"Case {case['case_id']} logged successfully.\n")

        elif choice == "5":
            search_case()

        elif choice == "6":
            print("Exiting system.")
            break

        else:
            print("Invalid option.")
