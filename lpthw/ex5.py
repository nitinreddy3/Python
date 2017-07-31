name = "Nitin Reddy"
age = 28
height = 73 
weight = 200
eyes = "Black"
teeth = "White"
hair = "Black"
height_in_cm = height * 2.54
weight_in_kg = weight * 0.45

print "Let's talk about %s." % name
print "He's %d inches tall." % height
print "He's %d pounds heavy." % weight
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (eyes, hair)
print "His teeth are usually %s depending on the coffee." % teeth
print "Weight in kg is %d." % weight_in_kg
print "Height in centimetre is %d." % height_in_cm

# this line is tricky, try to get it exactly right

print "If I add %d, %d, and %d I get %r" % (age, height, weight, age + height + weight)