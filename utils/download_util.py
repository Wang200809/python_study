import urllib.request
from urllib.parse import urlparse
import os
url = "http://www.py4e.com/code3/mbox-short.txt"
# retrieve document name from url
path = urlparse(url).path        # "/code3/mbox-short.txt"
filename = os.path.basename(path)

req = urllib.request.Request(
    url,
    headers={"User-Agent": "Mozilla/5.0"}   # pretend to be a browser
)

with urllib.request.urlopen(req) as response:
    data = response.read().decode("utf-8")

with open(filename, "w", encoding="utf-8") as f:
    f.write(data)

print(filename+" downloaded successfully")
