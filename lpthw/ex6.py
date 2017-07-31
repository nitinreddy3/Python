# Tell the types of people i find in the world
x = "There are %d types of people." % 10

# String declared as binary
binary = "binary"

# String declared as do_not
do_not = "don't"

# Interpolation of string value in side another string
y = "Those who know  %s and those who %s." % (binary, do_not)

print x
print y

# Interpolation of string value in side another string
print "I said: %r." % x
print "I also said: '%s'." % y

hilarious = False
joke_evaluation = "Isn't that joke so funny?! %r"

print joke_evaluation % hilarious

w = "This is the left side of..."
e = "a string with a right side."

print w + e