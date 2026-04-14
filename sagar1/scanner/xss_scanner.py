import requests

def check_xss(url):
    payload = "<script>alert('XSS')</script>"
    test_url = f"{url}?q={payload}"

    try:
        response = requests.get(test_url, timeout=5)

        if payload in response.text:
            return ["Reflected XSS detected on parameter 'q'"]

    except:
        pass

    return []