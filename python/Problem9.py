#!/usr/bin/python

a_val = 1
b_val = 2
c_val = 3

def testForWin(a, b, c):
    if (a + b + c) == 1000:
        if (math.pow(a, 2) + math.pow(b, 2)) == math.pow(c, 2):
            return True

def testCVal(c):

for test_c in range(c_val, 999):

    if testForWin(test_c):

