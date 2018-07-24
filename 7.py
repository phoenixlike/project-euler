'''
By listing the first six prime numbers: 
2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?
'''

import math

def isPrime(n):
        '''
        Optimised Student's method to check for Primality.
        '''
    
        #Check edge cases
        if n<= 1:
            return False
        if n<=3:
            return True
        #Check to skip 5 middle numbers
        #below
        if (n % 2 == 0 or n % 3 == 0):
            return False
        
        i = 5
        while i*i <= n:
            if (n % i == 0 or n % (i+2) == 0):
                return False
            i = i + 6
        return True

prime_list = []
i = 1

while len(prime_list) < 10001:
    if isPrime(i):
        prime_list.append(i)
    i = i+1

print prime_list[-1]

