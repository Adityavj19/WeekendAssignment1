c = raw_input("Enter First Number:")
d = raw_input("Enter Second Number:")

def add(a, b):
    print "adding %d + %d" % (a, b)
    return a + b

def subtract(a, b):
    print "subtracting %d - %d" % (a, b)
    return a - b

def multiply(a, b):
    print "multiplying %d * %d" % (a, b)
    return a * b

def divide(a, b):
    print "dividing %d / %d" % (a, b)
    return a / b


print "Let's do some math with just functions!"

age = add(23, 23)
height = subtract(100, 44)
weight = multiply(90, 5)
div = divide(30, 2)

print "Age: %d, Height: %d, Weight: %d, div: %d" % (age, height, weight, div)



print "Here is a puzzle."

what = add(age, subtract(height, multiply(weight, divide(div, 2))))

print "That becomes: ", what, "Can you do it by hand?"