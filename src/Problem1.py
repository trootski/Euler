'''
Created on Aug 19, 2011

@author: troot
'''


'''Find the sum of all the multiples of 3 or 5 below 1000.'''

final_sum_total = 0
i = 0

for i in range(1000):
	if (i%3) == 0 or (i%5) == 0:
		final_sum_total = final_sum_total + i
	
	i = i + 1

print "The answer is: %s" % final_sum_total