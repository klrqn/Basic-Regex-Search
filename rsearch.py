#! python3
# Opens all .txt files in a dir and searches for a user supplied expression

import os, re
from pathlib import Path

# Get Search Phrase From User
searchPhrase = input("What Word or Phrase would you like to search for?\n")

# Regex String
searchPhrase = re.compile(searchPhrase)

# Get Directory Location
searchDir = input("What directory would you like to search:\n")

# Validate Directory Location
while not Path(searchDir).is_dir():
    print("That is not a valid Directory, try again:\n")
    searchDir = input()

# create a list of all files
fileList = os.listdir(searchDir)

# loop through each file
for f in fileList:
    # get all text files in directory
    if f.endswith('.txt'):
        inFile = Path(searchDir) / f
        openFile = open(f)
        fileText = openFile.read()
        # print(fileText)
        # show which files have search phrase
        if searchPhrase.search(fileText):
            print(f'{f.ljust(20)} contains the phrase you are looking for')



