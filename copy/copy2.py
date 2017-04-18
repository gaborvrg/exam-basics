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

# print(sys.argv[1])

if len(sys.argv) == 1:  # if no argument
    print ('copy','[source]','[destination]')

elif len(sys.argv) <= 2 :
    print ('No destination provided' )

else:
    if os.path.isfile(sys.argv[1]) is True:
        print('File exists and write it to the destination!')
        src = str(sys.argv[1])
        dst = str(sys.argv[2])

        # print(str(sys.argv[1]),str(sys.argv[2]))

        handle = open(src, 'r')
        file = handle.read()
        handle.close()
        # print(file)

        handle = open(dst, 'w')
        for line in file:
            handle.write(line)
        handle.close()   


    else:
        print("file doesn\'t exists")
    
