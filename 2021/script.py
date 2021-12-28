# Script for creation of new files

import os

py_file = ""
txt_file = ""

# collect input
print("Enter name of new py file: ")
py_file = input()
print("Enter name of new txt file: ")
txt_file = input()

# format and create files
os.chdir("solution_files")
f = open(py_file + ".py", "w+")
f.close()

os.chdir("../input-files")
f = open(txt_file + ".txt", "w+")
f.close()