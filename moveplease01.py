#!/usr/bin/env python3

# Additional libraries to support code
import shutil
import os

# Example of best practice to function
def main():

    """ called at runtime
        Force python program to start in home user directory"""
    os.chdir('/home/student/mycode/')

    """ shutil.move(source, destination) move file or folder from A to B
        if file exists, it is overwritten"""
    shutil.move('raynor.obj', 'ceph_storage')

    # prompt user for a new name for the kerrigan file
    xname = input('What is the new name for kerrigan.obj? ')

    # rename current kerrigan obj file
    shutil.move('ceph_storage/kerrigan.obj', 'ceph_storage/' + xname)


main()
