import os
import sys
import math

def find_primes(n):
    is_prime_lst = [True]*(n+1)
    is_prime_lst[0] = False
    is_prime_lst[1] = False
    
    n_sqrt = int(math.sqrt(n))
    for i in range(2, n_sqrt, 1):
        if is_prime_lst[i] == True:
            for j in range(i*i, n, i):
                is_prime_lst[j] = False
    return [i for i in range(n+1) if is_prime_lst[i] == True]

if __name__ == '__main__':
    lst = find_primes(10000000)
    #print('result=%s'%(lst))
    print('count=%d'%(len(lst)))
