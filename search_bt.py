import urllib.request
import json
url = "https://api.github.com/search/code?q=repo:mctechnology17/zmk-config+dummy+vbatt"
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
with urllib.request.urlopen(req) as response:
    print(response.read().decode())
