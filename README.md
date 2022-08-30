# Hexhacks
A collection of small hacking tool I've built

##Checker.py
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
