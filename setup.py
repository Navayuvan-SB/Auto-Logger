"""=================================================
            Setup file for AutoLogger
================================================="""

# Import Statements
import os


# Print Welcome message
print("""
Welcome to AutoLogger Setup
This file will install AutoLogger in your machine and let you use the program as terminal command
""")


# Setup Method
def setup():

    # Upgrading pip
    print("Upgrading pip...")
    os.system("pip install --upgrade pip")
    print("Pip upgraded successfully...")

    # Instaling the requirements
    print("Installing the required package...")
    os.system('pip install -r requirements.txt')
    print("Required packages installed successfully...\n")

    # Make Log file as executable
    print("Giving execute permision to user...")
    os.system('chmod +x log')
    print("Permisson granted successfully...\n")

    # Move the log file to /bin
    print("Adding 'log' command to your terminal...")
    os.system('sudo cp log /bin')
    print("Command added successfully...\n")
    
    # Removing the log file in current location
    print("Removing the original log file...")
    os.system('rm log')
    print("File removed successfully...")

    # Printing Get Started message
    print("""
    Hurray...! The installation was completed successfully :)
    Close this Installation window and open a new one to use AutoLogger

    Run 'log --help' to read the user manual.
    """)

# Print conformation prompt
choice = input("Do you want to continue? [Y/n]")

# Decission making for the choice
if (choice == "Y" or choice == "Yes" or choice == "YES" or choice == "" or choice == "y"):

    # Call the setup function
    setup()

else:

    # Print Abort and exit the program
    print("Abort.")