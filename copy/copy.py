# This should be the basic replica of the 'cp' command
# If ran from the command line without arguments
# It should print out the usage:
# copy [source] [destination]
# When just one argument is provided print out
# No destination provided
# When both arguments provided and the source is a file
# Read all contents from it and write it to the destination

import sys
import os

if len(sys.argv) == 1:  # if no argument
    print ('copy','[source]','[destination]')

elif len(sys.argv) == 2 : # if there is only one arg 
    print ('No destination provided' )

else:
    if os.path.isfile(sys.argv[1]) is True: # check the source file exits
        print('File exists and write it to the destination!')
        source = str(sys.argv[1])
        destination = str(sys.argv[2])

        handle = open(source, 'r')
        file = handle.read() # read the file to a variable
        handle.close()

        handle = open(destination, 'w') # open a file to write
        for line in file:
            handle.write(line) # write line by line
        handle.close()   

    else:
        print("File doesn\'t exists")
    
