from sys import argv

script, input_file = argv

current_file = open(input_file)

def print_all(f):
    print f.read()

def rewind(f):
    f.seek(0)

print_all(current_file)

rewind(current_file)