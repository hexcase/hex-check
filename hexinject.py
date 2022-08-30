

import requests
import argparse
import json


############### Argparse stuff ###############

default = "%s" #For the %s in on of the arguments
parser = argparse.ArgumentParser(description='Url injector, takes a url with %s where you want to inject your list of arguments. Ex: https://www.example.com/search.php?p=\033[36;1m%s\033[0m&stuff=stuff')
#Had to use default.replace because argparse is being weird about %
parser.add_argument('-u', '--url', metavar='', type=str, required=True, help='The url you want to use, don\'t forget the %s' % default.replace(r"%", r"%%")) 
parser.add_argument('-f', '--file', metavar='', type=str, required=True, help='The list you want to inject, 1 argument per line')
parser.add_argument('-H', '--header', action='store_true', help='Prints the header response')
parser.add_argument('-s', '--statuscode', action='store_true', help='Prints the Status codes')
parser.add_argument('-nh', '--nohtml', action='store_true', help='Doesn\'t print the html response')
args = parser.parse_args()

##############################################



file1 = open(args.file, 'r')
lines = file1.readlines()



for line in lines:
    r2 = requests.get(args.url %(line.strip()))
    print(args.url %(line.strip()))
    
    if args.statuscode:
        print(r2.status_code)
    if args.header:
        print(json.dumps(dict(r2.headers), indent=2))
    if args.nohtml != True:
        print(r2.text)

