import requests

proxy_url = 'https://raw.githubusercontent.com/Ramxantanha/data/main/proxies.txt'

try:
    response = requests.get(proxy_url)
    if response.status_code == 200:
        proxies = response.text.strip().split('\n')
        print(proxies)
    else:
        print("Failed to fetch proxies from the provided URL.")
except requests.RequestException as e:
    print("An error occurred:", e)
