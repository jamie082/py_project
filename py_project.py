#!/usr/bin/python3

import datetime
import write

file_buffer = open("file.dat", "w")

try:
    string = input("How many lines to text file?: ")

    for p in file_buffer:
        print(file_buffer)

    try:
        print("Hello, test this out\n")

    except: # file didn't load
        print ("Couldn't load file: Error")

    finally: # close file when done
        f.close()

except:
    current_time = datetime.datetime.now() # date and time formatting, fix later
    print("\nCONTROL PANEL")
    print("> 15: " + string + " : " + (current_time.strftime("%m-%d-%Y")))
