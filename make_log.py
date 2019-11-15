""" ==================================================
                Auto Logging using Python
=================================================== """


# Import Statements
from datetime import datetime
import os.path

# Creating AutoLogger Directory if not exist
try:
    os.mkdir(os.path.expanduser("~/AutoLogger"))

except FileExistsError:
    pass

# Expanding the directory
path = os.path.expanduser(os.path.join("~/AutoLogger/", "my_log.txt"))

# Opening a file
f = open(path, "a+")

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

