from django.shortcuts import render
from .scanner.sql_scanner import check_sql_injection
from .scanner.xss_scanner import check_xss
from .scanner.header_scanner import check_security_headers
from .scanner.dir_scanner import directory_bruteforce


def safe_scan(scan_function, url):
    """Run scanner safely without breaking the app"""
    try:
        return scan_function(url)
    except Exception:
        return ["error"]


def scan(request):
    if request.method == "POST":
        url = request.POST.get("url", "").strip()

        # Validate input
        if not url:
            return render(request, "scan.html", {"error": "Please enter a valid URL"})

        # Run scans safely
        results = {
            "sql": safe_scan(check_sql_injection, url),
            "xss": safe_scan(check_xss, url),
            "headers": safe_scan(check_security_headers, url),
            "directories": safe_scan(directory_bruteforce, url),
        }

        # Convert results to status (True = Safe, False = Vulnerable)
        context = {
            "url": url,
            "sql_status": not results["sql"],
            "xss_status": not results["xss"],
            "header_status": not results["headers"],
            "dir_status": not results["directories"],
        }

        return render(request, "result.html", context)

    return render(request, "scan.html")
