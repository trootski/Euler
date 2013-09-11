'''
Created on Aug 19, 2011

@author: troot
'''

import math

def isPrime(num):
	
	is_num_prime = True
	
	sqrt_i = int( math.floor( math.sqrt( num ) ) )
	
	for j in range(2, sqrt_i + 1):
		if (num % j) == 0:
			is_num_prime = False
			break;
	
	'''if is_num_prime:
		print "%s is prime" % i
	else :
		print "%s is not prime" % i'''
	return is_num_prime

#for i in range(2, 100):
	

large_number = 600851475143

sqrt_large_number =  int( math.floor( math.sqrt( large_number / 2 ) ) )

for i in range(2, sqrt_large_number):
	
	if isPrime(i) and (large_number%i) == 0:
		print i
	

