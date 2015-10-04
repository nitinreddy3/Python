# storing a input accepted from a user in a variable
name = input("What's your name?: ")

#checking the name entered and executing the code based on the conditions
if name == "Nitin":
    print("{} is a lumberjack and he/she's ok".format(name))
else:
    print("{} sleeps all night and {} works all day!".format(name, name))
