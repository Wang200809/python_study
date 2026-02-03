import urllib.request

url = "http://www.py4e.com/code3/romeo.txt"

req = urllib.request.Request(
    url,
    headers={"User-Agent": "Mozilla/5.0"}   # pretend to be a browser
)

with urllib.request.urlopen(req) as response:
    data = response.read().decode("utf-8")

with open("romeo.txt", "w", encoding="utf-8") as f:
    f.write(data)

print("romeo.txt downloaded successfully")
