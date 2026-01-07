#!/usr/bin/python3

import sys

# This opens the file for reading if possible, if not it'll give you error message. 
def open_file_read(filename):
    try:
        file = open(filename, "r")
    except:
        print("Cannot open", filename)
        return None
    else:
        return file

# Builds a dictionary:  {county: total_cases}
def cases_dictionary_create(file):
    county_cases = {}
    for line in file:
        line = line.strip()
        if not line:
            continue
        city, county, cases = line.split(",")
        cases = int(cases)
        if county in county_cases:
            county_cases[county] += cases
        else:
            county_cases[county] = cases
    return county_cases

# Finds the county with the highest total number of cases
def highest_cases(county_cases):
    max_cases = 0
    max_county = ""
    for county in county_cases:
        cases = county_cases[county]
        if cases > max_cases:
            max_cases = cases
            max_county = county
    return max_county, max_cases

# --- Test Code ---
filename = input("File name: ")
file = open_file_read(filename)
if file:
    cases = cases_dictionary_create(file)
    file.close()
    max_county, max_cases = highest_cases(cases)
    print(max_county, max_cases)
