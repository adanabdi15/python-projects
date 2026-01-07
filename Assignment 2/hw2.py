#!/usr/bin/python3 

def open_file_read(filename):
	try:
	   	return open(filename, "r")
	except: 
		print("Error: could not open file", filename)
		return None 

def highest_score(file):
    max_score = 0
    max_name = ""
    for line in file:
        parts = line.split()
        score = int(parts[0])
        name = parts[1] + " " + parts[2]
        if score > max_score:
            max_score = score
            max_name = name
    return max_score, max_name 


filename = input("File name: ")
file = open_file_read(filename)
if file:
    score, name = highest_score(file)
    print()
    print("Highest score", score, name)
