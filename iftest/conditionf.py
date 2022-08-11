#!/usr/bin/env python3

# Collect input from user
hostname = input("What value should we set for hostname? ")

# user .lower() to somewhat validate input for checking mtg casing
if hostname.lower() == "mtg":
    print("The hostname was found to be mtg")
    print("The hostname matches expected config")

# Outside the if statement, state the leaving of the script even if they didnt enter
print("Exiting the script")
