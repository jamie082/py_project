#!/usr/bin/python3

import os.path
import fileinput

buffer_1 = open("alphabet.dat", "a") # create file buffer

try:

    # put at bottom of file
    print("\n")
    for line in fileinput.input(files = ("alphabet.dat")):
        #print ("Filename: ", fileinput.filename())
    
        for i in range(97, 123):
          buffer_1.write(chr(i))
          print("> Wrote letter " + chr(i) + " to file")


    print("\n")
    print ("Filename: \t", fileinput.filename())
    print("\n")

finally:
    buffer_1.close() # close file buffer
