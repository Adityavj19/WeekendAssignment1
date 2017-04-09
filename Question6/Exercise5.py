def print_1(*args):
    arg1, arg2 = args
    print "arg1: %r, arg2: %r" % (arg1, arg2)


def print_2(arg1, arg2):
    print "arg1: %r, arg2: %r" % (arg1, arg2)


def print_3(arg1):
    print "arg1: %r" % arg1


def print_none():
    print "I got nothin'."


print_1("Zed","Shaw")
print_2("Zed","Shaw")
print_3("First!")
print_none()