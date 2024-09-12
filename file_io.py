# Module: a file containing Python definitions and statements. A module's functions, classes, and global variables can be accessed by other modules.
# Package: a collection of modules that can be accessed as a group using the package name.
# import: the Python keyword used to access data from other packages and modules inside of the current module.
# PyPI: the Python Package Index. A repository of Python packages that can be downloaded and made available to your application.
# pip: the command line tool used to download packages from PyPI. pip is installed on your computer automatically when you download Python.
# Virtual Environment: a collection of modules, packages, and scripts that can be activated or deactivated at any time.
# Pipenv: a virtual environment tool that uses pip to manage the modules, packages, and scripts that you intend to use in your application.
# Mode represents the file's permissions.

# Pass in the name of the file as a string, must be in same cwd as the file reading code
# 'r' means read

L = []
with open('MyFile.txt', 'r') as F: # We can open the file in different modes, the default is read
    for s in F:
        L.append(s)

# OPEN
text_file = open('file_directory/file_name.txt')# Only required argument for the open function is the path to the file 

# Or we can specify the encoding
text_file = open('file_directory/file_name.txt', encoding='utf-8')

# CLOSE
text_file = open('file_name.txt', encoding='utf-8')
text_file.close()

# Use 'with' to prevent problems like forgetting to close a file
with open('file_name.txt', encoding='utf-8') as text_file:
    text_file.read()

# MODE
# The mode attribute of a file can tell you which mode the file has been opened in - 'r' is read, 'a' is append, 'w' is write
text_file = open('file_directory/file_name.txt')
print(text_file.mode)

# READ
# Reading from a file
text_file = open('text_file.txt', encoding='utf-8')
print(text_file.read())

with open('big_file.txt', encoding='utf-8') as text_file:
    for line in text_file:
        # Process the individual line
        print(line)

# WRITE
# Similar to reading from a file, but we have to open the file in write or append. We can use the write() function to write and append to the file
with open('log_file.txt', mode='w', encoding='utf-8') as log_file:
    log_file.write('Log 1')

with open('log_file.txt', mode='a', encoding='utf-8') as log_file:
    log_file.write('Log 2')


