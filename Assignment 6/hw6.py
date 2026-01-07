#!/usr/bin/env python3

#command line args and exit
import sys

#for running unix commands 
import os


#ensures 2 command line arguments are provided. Returns 2 arguments or quits if its less than 2. 
def get_2_args():
#includes script name so it must be >= 3. 
    if len(sys.argv) < 3:
#must match example in class notes. 
        script_name = os.path.basename(sys.argv[0])
        print(f"Usage: {script_name} FILENAME PATH") #script name 
        sys.exit(1) # quit script. 
#returns firs two command line arg 
    return sys.argv[1], sys.argv[2]

# creates a .py file only if name has no extension. 
def create_python_file(filename):
    if "." in filename:
        print("ERROR: The filename should not have an extension")
        sys.exit(1)

    filename = filename + ".py"
#Unix commands to run. 
    cmd_1 = f"touch {filename}"
    cmd_2 = f"chmod 755 {filename}"
# runs commands. 
    os.system(cmd_1)
    os.system(cmd_2)
# prints each entry in a valid directory. 
def print_directory(path):
#checks if the directory exists 
    if not os.path.isdir(path):
        print(f"ERROR: {path} is not a directory")
        sys.exit(1)
# list whatever in the directory. 
    contents = os.listdir(path)
    for entry in contents:
        print(entry)

#Test code. 

try:
    arg1, arg2 = get_2_args()
    print(arg1, arg2)
    create_python_file(arg1)
    print_directory(arg2)
except:
    pass
