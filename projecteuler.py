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
