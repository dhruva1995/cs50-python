# https://itunes.apple.com/search?entity=song&limit=1&term=weezer
import requests
import sys
import json

if len(sys.argv) < 2:
    sys.exit()
artist = sys.argv[1]
url = f"https://itunes.apple.com/search?entity=song&limit=100&term={artist}"
response = requests.get(url)
results = response.json()["results"]
for result in results:
    print(result["trackName"])
