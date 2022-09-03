# Hexhacks
A collection of small hacking tool I've built

## [Hexcheck.py](#)
### :heavy_check_mark: A URL Validator

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
### :syringe: A simple URL wordlist injector

Requirements: *requests*

Hexinject is a simple URL injector that takes a wordlist and a position in a url marked by %s to makes requests until the list is exhausted. It can print out the html response, header response and status code.

```
Verifies that a list of URLs are valid URLs, return their status codes, their headers and writes it to a JSON file.

optional arguments:
  -h, --help      show this help message and exit
  -f , --file     The list of files you want to check
  -o , --output   Give a filename to output the json file
  -q, --quiet     No CLI output, useful for when you only want the output exported to JSON

```
