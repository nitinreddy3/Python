# Create a formatter for all types of data
formatter = "%r %r %r %r"

# Format a list of numbers
print formatter % (1, 2, 3, 4)

# Format a list of strings
print formatter % ("one", "two", "three", "four")

# Format a boolean values
print formatter % (True, False, True, False)

# Format a list of sentences
print formatter % ("Hellos' World", 'My name is "nitin" reddy', "So good", "Gumanm")