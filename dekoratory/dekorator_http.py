import requests

def stahni():
    """Stáhne stránku a něco s ní udělá."""
    print("Stahuju stránku")
    odpoved = requests.get("https://httpbin.org/status/200,400,500")
    print(f"Dostali jsme {odpoved.status_code}")
    odpoved.raise_for_status()
    return "OK"


if __name__ == "__main__":
    stahni()