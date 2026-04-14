import requests

SQL_PAYLOADS = [
    "' OR 1=1 --",
    "\" OR \"\"=\"",
    "' OR 'a'='a",
    "' OR 1=1#",
]

def check_sql_injection(url):
    findings = []

    for payload in SQL_PAYLOADS:
        test_url = f"{url}?id={payload}"

        try:
            response = requests.get(test_url, timeout=5)
            error_words = ["sql", "syntax", "mysql", "error", "warning"]

            for word in error_words:
                if word in response.text.lower():
                    findings.append(f"Possible SQL Injection using payload: {payload}")
                    break

        except:
            continue

    return findings