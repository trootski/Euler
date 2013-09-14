#!/usr/bin/python

a_val = 1
b_val = 2
c_val = 3

def testForWin(a, b, c):
    if (a + b + c) == 1000:
        if (math.pow(a, 2) + math.pow(b, 2)) == math.pow(c, 2):
            return True

def testPyThag(a, b, c):
    if (math.pow(a, 2) + math.pow(b, 2)) == math.pow(c, 2):
        return True

for test_a in range(a_val, 999):
	if testPyThag(a_val, b_val, c_val):
		if testForWin(a_val, b_val, c_val):
			print "Answer is: %s + %s + %s" % (a_val, b_val, c_val)


for test_c in range(c_val, 999):

    if testForWin(test_c):

