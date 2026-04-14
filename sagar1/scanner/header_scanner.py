import requests

REQUIRED_HEADERS = [
    "Content-Security-Policy",
    "X-Frame-Options",
    "X-Content-Type-Options",
    "Strict-Transport-Security",
    "Referrer-Policy"
]

def check_security_headers(url):
    findings = []

    try:
        response = requests.get(url, timeout=5)

        for header in REQUIRED_HEADERS:
            if header not in response.headers:
                findings.append(f"Missing security header: {header}")

        return findings

    except:
        return ["Unable to fetch website for header scan"]