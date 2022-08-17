#!/usr/bin/python3
"""Alta3 Research - Exploring OpenAPIs with requests"""
# documentation for this API is at
# https://anapioficeandfire.com/Documentation

import requests
import pprint

AOIF_CHAR = "https://www.anapioficeandfire.com/api/characters/"

def name_finder(got_list):
    names = []
    for x in got_list:
        r = requests.get(x)
        decodedjson = r.json()
        names.append(decodedjson.get("name"))
    return names

def main():
        ## Ask user for input
        got_charToLookup = input("Pick a number between 1 and 1000 to return info on a GoT character! " )

        ## Send HTTPS GET to the API of ICE and Fire character resource
        gotresp = requests.get(AOIF_CHAR + got_charToLookup)

        ## Decode the response
        got_dj = gotresp.json()
        pprint.pprint(got_dj)

        for x in name_finder(got_dj.get("allegiances")):
            print(x)

        for x in name_finder(got_dj.get("books")):
            print(x)


if __name__ == "__main__":
        main()

