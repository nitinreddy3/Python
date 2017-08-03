from sys import argv

script, input_file = argv

current_file = open(input_file)

# Function to read all the data in a file
def print_all(f):
    print f.read()

def rewind(f):
    f.seek(0)

# Function to read data line by line
def print_a_line(line_count, f):
    print line_count, f.readline()

print_all(current_file)

rewind(current_file)

# Print a first line of data 
count_line = 1
print_a_line(count_line, current_file)

