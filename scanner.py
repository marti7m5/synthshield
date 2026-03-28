import re

def scan_text(text):
    results = []

    if re.search(r"\b[\w.-]+@[\w.-]+\.\w+\b", text):
        results.append("Email detected")

    if re.search(r"\b\d{3}[-.]?\d{3}[-.]?\d{4}\b", text):
        results.append("Phone number detected")

    return results


if __name__ == "__main__":
    sample = input("Enter text: ")
    findings = scan_text(sample)

    if findings:
        print("⚠️ Sensitive data found:")
        for f in findings:
            print("-", f)
    else:
        print("No sensitive data detected")
