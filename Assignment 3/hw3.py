#!/usr/bin/python3

def open_file_read(filename):
    try:
        return open(filename, "r")
    except:
        print("Error: could not open file", filename)
        return None

def student_dictionary_create(file):
    students = {}
    for line in file:
        line = line.strip()
        if not line:
            continue
        fields = line.split()
        if len(fields) >= 5:
            sid = fields[0]
            first, last, user, email = fields[1], fields[2], fields[3], fields[4]
            data = (first, last, user, email)
            students[sid] = data
    return students

def student_dictionary_print(students):
    for sid in sorted(students):
        first, last, user, email = students[sid]
        print(sid, first, last, user, email)

if __name__ == "__main__":
    filename = input("File name: ")
    file = open_file_read(filename)
    if file:
        students = student_dictionary_create(file)
        if students:
            student_dictionary_print(students)
