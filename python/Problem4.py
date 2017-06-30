'''
Created on Aug 19, 2011

@author: troot
'''

import math
import sys

#999 x 999 = 998,001
def isPalindrome(num):
	
	tmpStr = str(num)
	
	num_len = len(tmpStr)
	
	half_way = int(math.floor( num_len / 2 ))
	
	if half_way > 0:
		
		for i in range(half_way):
			if tmpStr[i] != tmpStr[num_len - i - 1]:
				return False
	
	return True

def has3DigitProducts(num):
	
	sqrt_num = int( math.floor( math.sqrt( num ) ) )
	
	if sqrt_num < 100:
		return False
	
	for i in range(sqrt_num, 100, -1):
		modulo_val = num%i
		if modulo_val == 0 and len(str(i)) == 3 and len(str(modulo_val)) == 3:
			print "Three digit factor = %s (large_num=%s)" % (i, num)
			return True
	
	return False
	

print has3DigitProducts(998001)
highest_pal = 0
for i in range(999, 100, -1):
    for j in range (999, 100, -1):
        #print "Checking number %s x %s" % (i, j)
        if isPalindrome(i * j):
            #print "Largest product is %s x %s = %s" % (i, j, i*j)
            if (i*j) > highest_pal:
                highest_pal = i*j
            #sys.exit();
print "Higest pal is: %s" % highest_pal
'''large_num = 999 * 999

for j in range(large_num, 0, -1):
	#print "Checking number: %s" % j
	if isPalindrome(j) and has3DigitProducts(j):
		print "Largest palindrome is %s" % j
		break'''
