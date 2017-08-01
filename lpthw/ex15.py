from sys import argv

# Arguments are script name and filename
script, filename = argv

# Assigns object returned from open method to the variable
txt = open(filename)

# Prints the accepted filename
print "Here's you file: %r" % filename

# Outputs the result of reading the file
print txt.read()