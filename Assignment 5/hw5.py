#!/usr/bin/env python3


# This fuction purpose is to open a file of reading. furthermore if the file doesn't open it gives  you a error message. 
def open_file_read(filename):
    try:
        file = open(filename, "r")
        return file
    except:
        print("Error: could not open file", filename)
        return None

# This part of the code reads each line from a file and adds thr words to a set, also removing copies. 

def set_from_file(file):
    s = set()
    for line in file:
        s.add(line.strip())
    return s

# Print each element in a set  in order by alphabet. 

def print_sorted_set(s):
    for element in sorted(s):
        print(element)

# Test code. 
file_1 = open_file_read("words_1.txt")
file_2 = open_file_read("words_2.txt")
if file_1 and file_2:
    set_1 = set_from_file(file_1)
    set_2 = set_from_file(file_2)
    print("set 1:", len(set_1), "elements")
    print("set 2:", len(set_2), "elements")
    print("Union sets 1 & 2:", len(set_1 | set_2), "elements")
    print("Intersection sets 1 & 2:", len(set_1 & set_2), "elements")
    print("Elements in intersection sets 1 & 2")
    print_sorted_set(set_1 & set_2) 

