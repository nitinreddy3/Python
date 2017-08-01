from sys import argv

# Arguments are script name and filename
script = argv

# Accept the file name from a user
filename = raw_input("Enter the file name: ")

# Assigns object returned from open method to the variable
txt = open(filename)

# Prints the accepted filename
print "Here's you file: %r" % filename

# Outputs the result of reading the file
print txt.read()