import urllib.request
import json
url = "https://api.github.com/search/code?q=repo:englmaxi/zmk-config+battery"
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
with urllib.request.urlopen(req) as response:
    data = json.loads(response.read().decode())
    for item in data.get('items', [])[:5]:
        print(f"{item['path']}")
