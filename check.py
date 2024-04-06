def get_proxies(proxy_url):
    try:
        response = requests.get(proxy_url)
        if response.status_code == 200:
            proxies = response.text.strip().split('\n')
            return proxies
        else:
            print("Failed to fetch proxies from the provided URL.")
            return []
    except requests.RequestException as e:
        print("An error occurred while fetching proxies:", e)
        return []
