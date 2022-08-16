#!/usr/bin/env python3

import re

def main():
    filetoreplace = input("Please name the file: ")
    keyword = input("What word/phrase would you like to find?: ")
    with open(filetoreplace, 'r') as doc:
        filetoparse = doc.read()

    filetoparse = filetoparse.replace(keyword, "*****")
    
    with open(filetoreplace, "w") as newdoc:
        newdoc.write(filetoparse)

if __name__ == "__main__":
    main()
