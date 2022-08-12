#!/usr/bin/env python3

import netifaces
def ipaddress(adapter):
    print('IP :', end='')
    print(adapter[0]['addr'])

def main():

    print(netifaces.interfaces())
    for i in netifaces.interfaces():
        #print(netifaces.ifaddresses(i))
        print('\n**************Details of Interface - ' + i + ' *********************')
        try:
            #print('MAC: ', end='')
            #print((netifaces.ifaddresses(i)[netifaces.AF_LINK])[0]['addr'])
            #print('IP: ', end='')
            #print((netifaces.ifaddresses(i)[netifaces.AF_INET])[0]['addr'])
            ipaddress(netifaces.ifaddresses(i)[netifaces.AF_INET])
        except:
             print('Could not collect adapter information')


main()
