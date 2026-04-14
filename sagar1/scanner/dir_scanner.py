import requests

COMMON_DIRS = [
    "admin/",
    "uploads/",
    "backup/",
    "config/",
    "test/",
    "data/",
    ".git/",
    "images/",
    "private/",
    "old/",
]

def directory_bruteforce(url):
    findings = []

    for directory in COMMON_DIRS:
        test_url = f"{url.rstrip('/')}/{directory}"

        try:
            response = requests.get(test_url, timeout=5)

            # Directory listing is usually "Index of /folder"
            if response.status_code == 200 and "Index of" in response.text:
                findings.append(f"Directory listing enabled: {test_url}")

        except:
            continue

    return findings
