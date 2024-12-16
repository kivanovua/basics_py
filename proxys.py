import requests

# Define the proxy server(s)
# Replace with your proxy details
proxies = {
    'http': 'http://username:password@proxyserver:port',  # HTTP proxy
    'https': 'http://username:password@proxyserver:port'  # HTTPS proxy
}

# Test the proxy connection
def test_proxy(proxy):
    try:
        print("Testing proxy...")
        response = requests.get('http://httpbin.org/ip', proxies=proxy, timeout=10)
        if response.status_code == 200:
            print("Proxy is working. Response:")
            print(response.json())
        else:
            print("Proxy failed with status code:", response.status_code)
    except requests.exceptions.RequestException as e:
        print(f"Proxy test failed: {e}")

# Make a request using the proxy
def fetch_data(url, proxy):
    try:
        response = requests.get(url, proxies=proxy, timeout=10)
        response.raise_for_status()  # Raise HTTPError for bad responses (4xx or 5xx)
        print("Request successful. Data fetched:")
        print(response.text)
    except requests.exceptions.RequestException as e:
        print(f"Request failed: {e}")

if __name__ == "__main__":
    # Test the proxy
    test_proxy(proxies)
    
    # Use the proxy to fetch data
    url_to_fetch = 'http://httpbin.org/get'
    fetch_data(url_to_fetch, proxies)