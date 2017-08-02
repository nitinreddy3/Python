# ok, that *args is actually pointless, we can just do this

first_name = raw_input("Please enter your name: ")

def print_name():
    print "My name is: %r" % first_name

print_name()
