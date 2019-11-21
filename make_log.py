#!/usr/bin/env python
# (For Command line Execution)
""" ==================================================
                Auto Logging using Python
=================================================== """
# Import Statements
from datetime import datetime
import os.path
import sys
import subprocess
import socket
import getpass
from termcolor import colored


# Log only the text which user enter
def text():

    # Initialise Flag as True
    flag = True

    # Get the input and write in the file
    while(flag):

        # Read the input from user
        log_text = input("Log:  ")

        # Check if the end condition satisfied
        if (log_text == ""):

            # Set the Flag to False and close the opened file
            flag = False
            f.close()
        
        else:

            # datetime object containing current date and time
            now = datetime.now()
    
            # dd/mm/YY H:M:S
            dt_string = now.strftime("%d/%m/%Y %H:%M:%S")

            # Format the text to write
            text_to_write = dt_string + " \t " + log_text + "\n\n"

            # Write to the file
            f.write(text_to_write) 

# Log the output of the command
def command():

    # List for get the commands as system arguments
    cmd = []
    for arg in sys.argv:
        cmd.append(arg)

    # Run the command through subprocess pipe
    out = subprocess.Popen(cmd[2:], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)

    # Expanding the directory
    path = os.path.expanduser(os.path.join("~/AutoLogger/", "my_terminal_log.txt"))

    # Opening a file
    f = open(path, "a+")

    # Print the output line by line
    for line in iter(out.stdout.readline, b''):
        temp = str(line)
        temp = temp[2: len(temp)-3]
        print (temp)
        f.write(temp)
        f.write("\n")

    f.close()

# Turn into Terminal Mode
def terminal():

    print("""
        Terminal Mode is started... Your all terminal activities will be logged into the log file
        Enter 'exit()' to exit terminal mode
        """)

    # Get the input untill exit() command is given
    while(True):

        # Print the terminal text
        term_starter = colored(getpass.getuser() + "@" + socket.gethostname(), 'green') + colored(":", 'white') + colored(os.getcwd(), 'blue') + "$ "
        cmd = input(term_starter)
        cmd = cmd.split(" ")
        if (cmd[0] == "exit()"):
            print("""
            Exiting Terminal Mode...
            """)
            break

        # Run the command through subprocess pipe
        out = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)

        # Expanding the directory
        path = os.path.expanduser(os.path.join("~/AutoLogger/", "my_terminal_log.txt"))

        # Opening a file
        f = open(path, "a+")

        # Write the command 
        f.write("Command: " + " ".join(cmd))
        f.write("\n")

        # Print the output line by line
        for line in iter(out.stdout.readline, b''):
            temp = str(line)
            temp = temp[2: len(temp)-3]
            print (temp)
            f.write(temp)
            f.write("\n")

        # Write a closing line for the command
        f.write("-----------------------------------------------------\n\n")

        # Closing the opened file
        f.close()

# Help manual
def help():
    
    # Printing the help manual
    print("""
    Usage: log [OPTIONS] [COMMAND]

    Options:
        [empty], -m, --message                  Type the log message and press 'Enter' to log into the file.
                                                Double tap 'Enter' to exit the program
        
        [command], -c, --command                Type the command and it will be logged with the output in
                                                my_terminal_log.txt file

        -t, --terminal                          Enter into terminal mode. The commands which you run will be
                                                logged with the output into my_terminal_log.txt file

    Additional Informations:
        ~ The output of the logs will be stored in 'AutoLogger' directory of your Home directory

        ~ You can use 'log' as alias of -m, --message

        ~ you can use 'log [command]' as alias of -c, --command

        ~ Use 'exit()' in 'Terminal mode' to exit 'Terminal mode'
    """)

# Create directory if not exists
def dir_check():

    # Creating AutoLogger Directory if not exist
    try:
        os.mkdir(os.path.expanduser("~/AutoLogger"))
        print("Seems like AutoLogger directory is missing :(")
        print("Creating AutoLogger directory in {%s} ...".format(os.path.expanduser("~")))
        print("AutoLogger was initialized successfully, Enjoy using AutoLogger :)")

    except FileExistsError:
        pass


# Directory Check
dir_check()

# Expanding the directory
path = os.path.expanduser(os.path.join("~/AutoLogger/", "my_log.txt"))

# Opening a file
f = open(path, "a+")

# If the option was to log the text user type

if (len(sys.argv) == 1):
    text()

elif (sys.argv[1] == "--message" or sys.argv[1] == "-m"):
    text()

# If the option was to log with the output from the terminal command
elif (sys.argv[1] == "--command" or sys.argv[1] == "-c" and len(sys.argv) > 1):
    command()

# If the option was terminal mode
elif (sys.argv[1] == "--terminal" or sys.argv[1] == "-t"):
    f.close()
    terminal()

# If the option was help
elif (sys.argv[1] == "--help"):
    f.close()
    help()