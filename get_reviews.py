import requests

proxies = {
   'http': 'http://127.0.0.1:7777',
   'https': 'http://127.0.0.1:7777',
}

url = 'https://www.amazon.com/32GB-Mp3-Player-Bluetooth-5-0/dp/B08CVR9PVS'


response = requests.get(url, proxies=proxies)
print(response.content)

