from sys import argv

script, user_name = argv
adi = '> '

print "Hi %s, I'm the %s script." % (user_name, script)
print "I'd like to ask you a few questions."
print "Do you like me %s?" % user_name
likes = raw_input(adi)

print "Where do you live %s?" % user_name
lives = raw_input(adi)

print "What kind of computer do you have?"
computer = raw_input(adi)

print """
Alright, so you said %r about liking me.
You live in %r.  Not sure where that is.
And you have a %r computer.  Nice.
""" % (likes, lives, computer)
