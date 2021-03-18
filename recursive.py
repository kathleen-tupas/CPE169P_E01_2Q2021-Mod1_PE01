"""
File: recursive.py

Prints a trace of a recursive function.
"""

import os

def displayFiles(pathname):
    """Returns name of file and its contents"""
    if os.path.isfile(pathname):
        name = os.path.basename(pathname)
        openFile = open(pathname, "r")
        fileContents = openFile.readlines()
        for eachContent in fileContents:
            print(eachContent)
            
    elif os.path.isdir(pathname):
        getDirectories = os.listdir(pathname)
        for eachItem in getDirectories:
            completePath = os.path.join(pathname, eachItem)
            print("Filename: ", completePath)
            isdirectory = os.path.isdir(completePath)
            if isdirectory or os.path.isfile(completePath):
                displayFiles(completePath)

"""A simple test."""
pathname = input("Enter the filename or directory path: ")
displayFiles(pathname)    
