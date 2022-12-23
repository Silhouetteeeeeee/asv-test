import requests
import json

url = "https://pv.github.io/numpy-bench/regressions.json"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 Edg/108.0.1462.46"
}

proxies={
'http': None,
'https': '127.0.0.1:10809'  # https -> http
}

r = requests.get(url=url, headers=headers, proxies=proxies)
results = r.json()['regression']


