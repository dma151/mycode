#!/usr/bin/env python3

import requests

POSTURL = "http://validate.jsontest.com/"

def main():

    # PART A
    dateres = requests.get("http://date.jsontest.com")
    json = dateres.json()
    print(json)

    # PART B
    ipres = requests.get("http://ip.jsontest.com")
    json2 = ipres.json()
    print(json2)
    
    # PART C
    with open('myservers.txt', 'r') as servers:
        list = servers.readlines()
        
    print(list)
    
    # PART D
    final = {"json": {"time" : json, "ip" : json2, "mysvrs": list}}
    print(final)
    
    # PART E
    call = requests.post("http://validate.jsontest.com", data=final)
    finalres = call.json()
    print(finalres)



if __name__ == "__main__":
    main()
