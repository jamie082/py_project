#!/usr/bin/python3

import os.path
import fileinput

buffer_1 = open("alphabet.dat", "w+") # create file buffer

try:
    for i in range(97, 123):
         buffer_1.write(chr(i))

    print("Wrote to file ", fileinput.filename())

finally:
    buffer_1.close() # close file buffer
