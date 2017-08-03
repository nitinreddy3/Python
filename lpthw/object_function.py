my_name = raw_input("Enter name: ")
my_age = raw_input("Enter age: ")
my_height = raw_input("Enter height: ")

class Person:
    def __init__(self, name, age, height):
        self.name = name
        self.age = age
        self.height = height

person_details = Person(my_name, my_age, my_height)

def print_details(obj):
    print "Name: %r" % obj.name
    print "Age: %r" % obj.age
    print "Height: %r" % obj.height

print_details(person_details)
