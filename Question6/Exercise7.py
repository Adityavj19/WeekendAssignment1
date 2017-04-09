from sys import argv

script, input_file = argv

current_file = open(input_file)
f = current_file

def print_all(f):
    print f.read()

print "First let's print the whole file:\n"
print_all(current_file)

def rewind(f):
    f.seek(0)

rewind(current_file)
print "Now let's rewind, kind of like a tape."

print "Let's print three lines:"
def print_a_line(line_count, f):
    print line_count, f.readline()


current_line = 1
print_a_line(current_line, current_file)
current_line = current_line + 1
print_a_line(current_line, current_file)
current_line = current_line + 1
print_a_line(current_line, current_file)