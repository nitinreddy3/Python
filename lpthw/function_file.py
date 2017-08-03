from sys import argv

script, input_file = argv

current_file = open(input_file)

def print_all(f):
    print f.read()

def rewind(f):
    f.seek(0)

def print_a_line(line_count, f):
    print line_count, f.readline()

print_all(current_file)

rewind(current_file)

count_line = 1
print_a_line(count_line, current_file)

