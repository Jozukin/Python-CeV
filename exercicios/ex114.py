import requests


def check_url(link):
    try:
        response = requests.get(link)
        if response.status_code == 200:
            return True
        else:
            return False
    except requests.exceptions.RequestException as e:
        return False


url = "https://www.google.com"
if check_url(url):
    print(f"A URL {url} está acessível.")
else:
    print(f"A URL {url} não está acessível.")
