# ok, that *args is actually pointless, we can just do this

first_name = raw_input("Please enter your name: ")

def print_name() -> object:
    assert isinstance(first_name, object)
    print ("My name is: %r" % first_name)

print_name()
