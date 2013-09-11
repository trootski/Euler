'''
Created on Aug 19, 2011

@author: troot
'''

num = 1
prev_num = 0
total_sum = 0

for i in range(1000000):
	
	tmp = num
	num = prev_num + num
	prev_num = tmp
	
	if num > 4000000:
		break
	
	if (num%2) == 0:
		total_sum = total_sum + num
		print "%s" % num

print "Answer: %s" % total_sum
	