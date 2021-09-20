#!/usr/bin/python3

try:
    f = open("test.txt")
    f.write("Added file content!")

except:
    print ("Couldn't load file: Error")

finally:
    f.close()
