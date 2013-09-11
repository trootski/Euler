#!/usr/bin/python

import math


def isPrime(num):

    sqrt_i = int( math.floor( math.sqrt( num ) ) )

    for j in range(2, sqrt_i + 1):
        if (num % j) == 0:
            return False

    return True

prime_number_count = 0
i = 2

while True:

    if isPrime(i):
        prime_number_count = prime_number_count + 1
        
        if prime_number_count == 10001:
            break
    
    i = i + 1

print "The 100001st prime number is %s" % i 

