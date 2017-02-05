import math as m
import itertools
import time
import numpy as np

#return nth fibonacci #
def  fib(n):
    return ((1 + sqrt(5)) ** n - (1 - sqrt(5)) ** n) / (2 ** n * sqrt(5))

#return boolean if prime
def  isPrime(n):
    for i in range(2, n // 2 + 1):
        if n % i == 0:
            return False
    return True

def  isPrime2(n):
    # http://stackoverflow.com/questions/2068372/fastest-way-to-list-all-primes-below-n-in-python/3035188#3035188
    """ Input n>=6, Returns a array of primes, 2 <= p < n """
    sieve = np.ones(n/3 + (n%6==2), dtype=np.bool)
    sieve[0] = False
    for i in range(int(n**0.5)//3+1):
        if sieve[i]:
            k=3*i+1|1
            sieve[      ((k*k)/3)      ::2*k] = False
            sieve[(k*k+4*k-2*k*(i&1))/3::2*k] = False
    return np.r_[2,3,((3*np.nonzero(sieve)[0]+1)|1)]

#return sum of digits
def  d(k):
    sum = 0
    for i in str(k):
        sum += int(i)
    return sum

#return factorial n!
def  factorial(n):
    if n == 2:
        return 2
    else:
        return n * factorial(n-1)

#return boolean, works for ints and strings
def  isPalindrome(n):
    stack = list(str(s))
    revStack = stack[::-1]
    for i in range(len(stack)):
        if stack[i] is not revStack[i]:
            return False
    return True


#return prime factors in list
def  primeFactors(n):
    f = 2
    increments = itertools.chain([1, 2, 2], itertools.cycle([4, 2, 4, 2, 4, 6, 2, 6]))
    for incr in increments:
        if f * f > n:
            break
        while n % f == 0:
            yield f
            n //= f
        f += incr
    if n > 1:
        yield n

#return arithmetic derivative when passed list of primes
def  arithDer(lst:list):
    quot = 1
    sum = 0
    for i in range(len(lst)):
        lst2 = (lst[j] for j in range(len(lst)) if j is not i)
        for j in lst2:
            quot *= j
        sum += quot
        quot = 1
    return sum

#
def  nameScore(n, pos):
    sum = 0
    for char in n:
        char.upper()
        sum += ord(char) % 64
    return sum * pos

def  collatz(n):
    lst = []
    if n == 1:
        return lst.append(n)
    if n % 2:
        n /= 2
    else:
        n = 3 * n + 1
    lst.append(collatz(n))

start = time.time()
print(arithDer(primeFactors(20)))
print(time.time() - start)
'''
The arithmetic derivative is defined by

p' = 1 for any prime p
(ab)' = a'b + ab' for all integers a, b (Leibniz rule)
For example, 20' = 24

Find ∑ gcd(k,k') for 1 < k ≤ 5·1015

Note: gcd(x,y) denotes the greatest common divisor of x and y.

+++++++++++++++++++++

There are some prime values, p, for which there exists a positive integer, n, such that
the expression n3 + n2p is a perfect cube.

For example, when p = 19, 83 + 82×19 = 123.

What is perhaps most surprising is that for each prime with this property the value of n is
unique, and there are only four such primes below one-hundred.

How many primes below one million have this remarkable property?
'''
