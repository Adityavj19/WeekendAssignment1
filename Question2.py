#Question-2 Write a program that accepts sequence of lines as input and prints the lines after making all characters in the sentence capitalized.
#Suppose the following input is supplied to the program:
#Hello world
#Practice makes perfect
#Then, the output should be:
#HELLO WORLD
#PRACTICE MAKES PERFECT


line_list = []

n = 2

for small_lines in range(n):
    input = raw_input("Enter Your Line: ")
    line_list.append(str(input.upper()))

for capital_lines in line_list:
    print "Your Line is - %s" % capital_lines
