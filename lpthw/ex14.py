from sys import argv

script, user_name = argv
prompt = '> '

print "Hi %s, I'm the %s script." % (user_name, script)
print "I'd like to ask you a few questions."
print "Do you like me %s?" % user_name
likes = raw_input(prompt)

if likes == "y":
    print "That's so cute of you!"

print "Where do you live %s?" % user_name
lives = raw_input(prompt)

if lives == 'pune':
    print "Which country does it belong to ?"
    country = raw_input(prompt)

print "What kind of computer do you have?"
computer = raw_input(prompt)

print """
Alright, so you said %r about liking me.
You live in a city %r which is in %r. Not sure where that is.
And you have a %r computer. Nice.
""" % (likes, lives, country, computer)