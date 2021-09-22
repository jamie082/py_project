#!/usr/bin/python3

import datetime
import write

try:
    string = input("How many lines to text file?: ")

    file_buffer = open("file.dat", "w+")

    for i in file_buffer:
      f.write("Added file content!")
      print(file_buffer)

    try:
        file_buffer.write("Lorum Ipsum\n")
        file_buffer.write("Write again\n")

    except: # file didn't load
        print ("Couldn't load file: Error")

    finally: # close file when done
        f.close()

except:
    current_time = datetime.datetime.now() # date and time formatting, fix later
    print("> 15: " + string + " : " + (current_time.strftime("%m-%d-%Y")))
