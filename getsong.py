import sys
import json
import requests

def main():
    if len(sys.argv) != 2:
        sys.exit("Too few arguments")
    
    resp = requests.get("https://itunes.apple.com/search?entity=song&limit=5&term="+sys.argv[1])
    
    o = resp.json()
    for result in o["results"]:
        print("Name:"+result["trackName"])



main()