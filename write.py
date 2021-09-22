#!/usr/bin/python3

import os.path

buffer_1 = open("alphabet.dat", "w+") # create file buffer

try:
    for i in range(97, 123): # create A through Z
         buffer_1.write(chr(i))

    print("Wrote to file %d", buffer_1)

finally:
    buffer_1.close() # close file buffer
