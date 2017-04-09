from sys import argv

script, filename = argv

print "We're going to erase %r." % filename
print "If you don't want that, hit CTRL-C (^C)."
print "If you do want that, hit RETURN."

raw_input("?")

print "Opening the file..."
dog = open(filename, 'w')

print "Truncating the file.  Goodbye!"
dog.truncate()

print "Now I'm going to ask you for three lines."

line1 = raw_input("line 1: ")
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")

print "I'm going to write these to the file."

dog.write(line1)
dog.write("\n")
dog.write(line2)
dog.write("\n")
dog.write(line3)
dog.write("\n")

print "And finally, we close it."
dog.close()