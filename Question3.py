#Question-3 Define a function that can accept two strings as input and print the string with maximum length in console.
#If two strings have the same length, then the function should print al l strings line by line.


string1 = raw_input("Enter first String:")
string2 = raw_input("Enter second String:")

def CompareString(string1,string2):
    l1 = len(string1)
    l2 = len(string2)
    if l1 > l2:
        print "Length of %s is greater" % string1
    elif l2 > l1:
        print "Length of %s is greater" % string2
    else:
        print "Length of %s and %s are equal" % (string1,string2)

CompareString(string1, string2)
