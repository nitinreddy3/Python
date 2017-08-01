from sys import argv

script, user_name = argv
prompt = '> '


# Accept the values passed as params from terminal
print "Hi %s, I'm the %s script." % (user_name, script)
print "I'd like to ask you a few questions."
print "Do you like me %s?" % user_name

# Accept like as yes or no from a user
likes = raw_input(prompt)

# Condition to execute print statement if a user input is y from previous statement
if likes == "y":
    print "That's so cute of you!"

print "Where do you live %s?" % user_name

# Accept the residing city of a user
lives = raw_input(prompt)

if lives == 'pune':
    print "Which country does it belong to ?"
    
    # Accept the residing country of a user        
    country = raw_input(prompt)

print "What kind of computer do you have?"

# Accept the type of computer a user uses
computer = raw_input(prompt)

print """
Alright, so you said %r about liking me.
You live in a city %r which is in %r. Not sure where that is.
And you have a %r computer. Nice.
""" % (likes, lives, country, computer)