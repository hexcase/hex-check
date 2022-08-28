
import json
import requests
import argparse


parser= argparse.ArgumentParser(description='Verify if a list of url are valid, return their status code, and return their headers in a json')
parser.add_argument('-f', '--file', type=str, metavar='', required=True, help='The list of files you want to check')
parser.add_argument('-q', '--quiet', action='store_true',  help='No outputs, useful for when you only want the output exported to JSON')

args = parser.parse_args()


httperror = {
        1: "Informational Response",
        2: "\033[22;1;3mSuccess\033[0m",
        3: "\033[36;1mRedirect\033[0m",
        4: "\033[37;41;1mClient Error\033[0m",
        5: "\033[34;41;1mServer Error\033[0m",
}


def checkr(url):
    
    r = requests.get(url, allow_redirects=False)
    
    # Format the JSON output
    fulllist = {
            "url": url,
            "status_code": r.status_code,
            "header": dict(r.headers),
            }
    jscon = json.dumps(dict(fulllist), indent=2)
    if not args.quiet:
        v = str(r.status_code)
        print(url, r.status_code, httperror[int(v[0])])

########## End of checkr ###########

def readlist(inlist):
    
    file1 = open(inlist, 'r')
    lines = file1.readlines()
    
    for line in lines:
        if (line.strip()[0:7] == "http://" or line.strip()[0:8] == "https://"): 
            inl = line.strip()
        else:
            inl = "http://" + line.strip() 
        checkr(inl)
########## End of readlist ########## 


if __name__ == '__main__':

    readlist(args.file)


