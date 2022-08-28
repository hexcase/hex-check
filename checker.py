
import json
import requests

def checkr(url):
    
    r = requests.get(url, allow_redirects=False)
    
    fulllist = {
            "url": url,
            "status_code": r.status_code,
            "header": dict(r.headers),
            }
    jscon = json.dumps(dict(fulllist), indent=2)
    print(jscon)


# checkr("http://perdu.com/")

file1 = open('list.txt', 'r')
lines = file1.readlines()

for line in lines:
    if line.strip()[0:4] != "http":
        lin = "http://" + line.strip()
    else:
        lin = line.strip()
    checkr(lin)
