#!/usr/bin/env python3

import requests
import argparse
import sqlite3
import threading
import time

# Html and URL parsing libraries
from bs4 import BeautifulSoup
from urllib.parse import urlparse

###### Hardcoded variables to be parsed
url = "https://ENTER URL HERE/"
numth = 10
attempts = 3 # For threading, attemps before closing thread
sleeptime = 3 # in seconds

#####################################################################

# Checks if urls are internal/external and stores them in the db
def checker(href):
    if 'http://' in href or 'https://' in href:
        
        # Possibly External
        if urlparse(href).hostname == purl.hostname:
            # Compared hostnames matches and is thus internal
            cur.execute('INSERT OR IGNORE INTO webcrawl(url, read, external) VALUES (?, ?, ?)', (href, 0, 0))
            print('Internal: ' + href)

        else:
            # Else if hostnames do not match, it's external
            cur.execute('INSERT OR IGNORE INTO webcrawl(url, read, external) VALUES (?, ?, ?)', (href, 0, 1))
            print('External: ' + href)

    else:
        # Assumes that any link with no http:// or https:// prefix is internal.
        if href[0] == '/':
            entry = url[:-1] + href
        else:
            entry = url + href
            cur.execute('INSERT OR IGNORE INTO webcrawl(url, read, external) VALUES (?, ?, ?)', (entry, 0, 0))
            print('Internal: ' + entry)
    con.commit()


# Pulls link from DB, handles attempts and starts req to crawl
def pulllink():
    cur2 = con.cursor()
    qry = cur2.execute('SELECT url FROM webcrawl WHERE external = 0 AND read = 0 LIMIT 1;') 
    try:
        pull = cur2.fetchone()[0]
        cur2.close()
    except:
        pull = ''
        cur2.close()
    else:
        print('PULLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLL ' + pull)
       

       ##################THIS IS WRONG THIS IS WRONG THIS IS WRONG ##########################
        # This currently behaves incorrectly, this should in theory catches attempts, but its only attempting to suck balls
        # Or maybe not, I'm not sure
        tries = 0
        while tries < attempts:
            if pull == '':
                tries += 1
                time.sleep(sleeptime)
                print('Waiting')
            else:
                tries += attempts
        ####################################################################################
        cur2 = con.cursor()
        cur2.execute('UPDATE webcrawl SET read = 1 WHERE url = ?', (pull,))
        cur2.close()
        print('READING FUCK IDFK MAN ' + pull)
        time.sleep(1)
        req(pull)
# Crawls for links
def req(pull):
    try:
        r = requests.get(url)
    except:
        print("Error, check url or connection")
    else:
        # Finding links in parsed html
        soup = BeautifulSoup(r.text, "html.parser")
        for link in soup.find_all("a"):
           checker(link.get("href"))
    pulllink()    

#####################################################################


#Set up the url so that its hostname is extractable
purl = urlparse(url)

#Setting up the Datatbase
con = sqlite3.connect(purl.hostname.replace(".","").replace("http://","").replace("https://","") + ".hxc", check_same_thread=False)
cur = con.cursor()
cur.execute("CREATE TABLE IF NOT EXISTS webcrawl(url PRIMARY KEY, read, external)")

#Initial request before threading
try:
    r = requests.get(url)
except:
    print("Error, check url or connection")
else:
    # Finding links in parsed html
    soup = BeautifulSoup(r.text, "html.parser")
    for link in soup.find_all("a"):
       checker(link.get("href"))
    
    # Threading
    ts = 0
    while ts < numth:
        time.sleep(1)
        ts += 1
        t = threading.Thread(target=pulllink)
        t.start()

