from sys import argv

script, filename = argv

txt = open(filename)

a = txt.read()

print "Here's your file %r:" % filename
print a

print "Type the filename again:"
file_again = raw_input("> ")

txt_again = open(file_again)

print txt_again.read()