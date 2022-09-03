#!/usr/bin/env python3

import requests
import argparse
import json
import threading

parser = argparse.ArgumentParser(description='Verifies that a list of URLs are valid URLs, return their status codes, their headers and writes it to a JSON file.')
parser.add_argument('-f', '--file', metavar='', type=str, required=True, help='The list of files you want to check')
parser.add_argument('-o', '--output', metavar='', type=str, help='Give a filename to output the json file')
parser.add_argument('-q', '--quiet', action='store_true', help='No CLI output, useful for when you only want the output exported to JSON')
args = parser.parse_args()

httperror = {
        1: "Informational Response",
        2: "\033[22;1;3mSuccess\033[0m",
        3: "\033[36;1mRedirect\033[0m",
        4: "\033[37;41;1mClient Error\033[0m",
        5: "\033[34;41;1mServer Error\033[0m",
}


def req(url):
    try:
        r = requests.get(url, allow_redirects=False)
    except:
        if args.output:
            of = open(args.output, 'a')
            fulllist = {
                    'url': url,
                    'status_code': 404,
                    }
            jscon = json.dumps(dict(fulllist), indent=2)
            of.write(jscon)
            of.write('\n')
            of.close()
        if args.quiet != True: 
            print(url, 'Unhandled 404', httperror[4])

    else:
        if args.output:
            of = open(args.output, 'a')
            fulllist = {
                    'url': url,
                    'status_code': 404,
                    'header': dict(r.headers),
                    }
            jscon = json.dumps(dict(fulllist), indent=2)
            of.write(jscon)
            of.write('\n')
            of.close()
        if args.quiet != True:    
            sc = str(r.status_code)
            print(url, " ", sc, httperror[int(sc[0])] )

def urlcleaner(line):
    if (line.strip().lower()[0:7] == "http://" or line.strip().lower()[0:8] == "https://"):
        req(line.strip().lower())
    else:
        req("https://" + line.strip().lower())



file1 = open(args.file, 'r')
lines = file1.readlines()

for line in lines:
    t = threading.Thread(target=urlcleaner, args=(line,))
    t.start()
