import requests


def call_api(url):
    response = requests.get(url)
    if response.status_code == 200:
        print("Success!")
    elif response.status_code == 404:
        print("Not Found!")


call_api("https://api.github.com")