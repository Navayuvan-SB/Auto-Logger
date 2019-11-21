# Import Statements
import sys
import subprocess
import os

# List for get the commands as system arguments
cmd = []
for arg in sys.argv:
	cmd.append(arg)

# Run the command through subprocess pipe
out = subprocess.Popen(cmd[1:], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)

# Expanding the directory
path = os.path.expanduser(os.path.join("~/AutoLogger/", "temp.txt"))

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