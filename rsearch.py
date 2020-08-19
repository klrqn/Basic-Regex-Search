#! python3
# Opens all .txt files in a dir and searches for a user supplied expression

import os, re
from pathlib import Path

# Get Search Phrase From User
searchPhrase = input("What Word or Phrase would you like to search for?\n")

# TODO: 2. Regex String
searchPhrase = re.compile(searchPhrase)

# Get Directory Location
inFile = input("What File would you like to search for?")

# TODO: a. Validate File Location


# TODO: Find all .txt files in directory

# TODO: Loop through each file
# TODO: Search contents of file for expression

# TODO: Print to Terminal
