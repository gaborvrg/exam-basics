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
    print ('copy','[source]','[destination]' )
elif len(sys.argv) == 2 :
    print ('No destination provided' )
else:
    if os.path.isfile(sys.argv[1]) is True:
        print('file exists')
    else:
        print("file doesn\'t exists")
    









# if len(sys.argv) == 1:
#     os.system('clear')
#     self.help_txt()
# else:
#     if ( sys.argv[1] == '-l' ):
        
#         db.open_db(self.file, self.arg)
#         db.view()

#     elif ( sys.argv[1] == '-a' ):
#         if len(sys.argv) == 2:
#             os.system('clear')
#             print('\n', 'Unable to add: no task provided' ,'\n')
#             db.open_db(self.file, self.arg)
#             db.view()
#         else:



















# from sys import argv # important ti run in terminal, not editor

# script, user_name = argv
# prompt = '> '

# print(argv[1])
# print(f"Hi {user_name}, I'm the {script} script.")
# print("I'd like to ask you a few questions.")
# print(f"Do you like me {user_name}?")
# likes = input(prompt)

# print(f"Where do you live {user_name}?")
# lives = input(prompt)

# print("What kind of computer do you have?")
# computer = input(prompt)

# print(f"""
# Alright, so you said {likes} about liking me.
# You live in {lives}.  Not sure where that is.
# And you have a {computer} computer.  Nice.