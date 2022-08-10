#!/usr/bin/env python3

# create list containing 3 tiems
my_list = [ "192.168.0.5", 5060, "UP" ]

#first print
print("The first item in the list (IP): " + my_list[0] )

#second
print("The second item in the list (port): " + str(my_list[1]) )

#third
print("The last item in the list (state): " + my_list[2] )

# Challenge

iplist = [ 5060, "80", 55, "10.0.0.1", "10.20.30.1", "ssh" ]

# only IPs (3 , 4)
print(f"The IP addresses in this list are: {iplist[3]} and {iplist[4]}")
