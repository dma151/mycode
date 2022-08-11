#!/usr/bin/env python3

# additional libraries to support our code
import shutil
import os

# Forces Python program to "start" in the home user directory
# No matter where prgram is accessed from, program will run from chdir(location)
os.chdir("/home/student/mycode/")

# shutil.copy(source, destination)
# copies a single file
shutil.copy("5g_research/sdn_network.txt", "5g_research/sdn_network.txt.copy")

# copies an entire folder
shutil.copytree("5g_research/", "5g_research_backup/")
