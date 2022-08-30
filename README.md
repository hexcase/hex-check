# Hexhacks
A collection of small hacking tool I've built

## [Hexcheck.py](#)
### A URL Validator

Requirements: *requests*

Hex-check is a simple url validator that takes a list of url as an input, returns the status code and parse both the status code and the header response in a json file.

```
usage: checker.py [-h] -f  [-q] [-o]

Verify if a list of url are valid, return their status code, and return their headers in a json

optional arguments:
  -h, --help      show this help message and exit
  -f , --file     The list of files you want to check
  -q, --quiet     No outputs, useful for when you only want the output exported to JSON
  -o , --output   Give a file name to output the json file
```
## [Hexinject.py](#)
### A simple URL wordlist injector

Requirements: *requests*

Hexinject is a simple URL injector that takes a wordlist and a position in a url marked by %s to makes requests until the list is exhausted. It can print out the html response, header response and status code.

```
usage: hexinject.py [-h] -u  -f  [-H] [-s] [-nh]

Url injector, takes a url with %s where you want to inject your list of arguments. Ex: https://www.example.com/search.php?p=%s&stuff=stuff

optional arguments:
  -h, --help        show this help message and exit
  -u , --url        The url you want to use, don't forget the %s
  -f , --file       The list you want to inject, 1 argument per line
  -H, --header      Prints the header response
  -s, --statuscode  Prints the Status codes
  -nh, --nohtml     Doesn't print the html response
```
