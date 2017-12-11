from collections import Counter
from itertools import repeat, takewhile
from fractions import Fraction

def multiply(numbers):
    result = 1
    for n in numbers:
        result *= n
    return result

class Primes:
    def __init__(self, n):
        N = n // 2
        sieve = [True] * N
        for i in range(3,  int(n**0.5) + 1, 2):
            if sieve[i // 2]:
                start = i ** 2 // 2
                sieve[start::i] = repeat(False, len(range(start, N, i)))
        self._list = [2] + [2*i+1 for i in range(1, N) if sieve[i]]
        self._set  = set(self._list)
        self.maxn  = n 
        
    def upto(self, n):
        if self.maxn < n:
            self.__init__(max(n, 2 * self.maxn))
        return takewhile(lambda x: x <= n, self._list)

class Factors:
    def __init__(self, maxn):
        self.largest = [1] * maxn
        for p in primes.upto(maxn):
            self.largest[p::p] = repeat(p, len(range(p, maxn, p)))
                    
    def totient(self, n):
        return int(n * multiply(1 - Fraction(1, p) for p in set(self(n))))
      
    def __call__(self, n):
        result = []
        if n >= len(self.largest):
            for p in primes:
                while n % p == 0:
                    result.append(p)
                    n = n // p
                if n < len(self.largest):
                    break
        while n > 1:
            p = self.largest[n]
            result.append(p)
            n = n // p
        return result


toti = dict()
def chain_size(n):
    if n == 1: return 1
    if n not in toti: toti[n] = 1 + chain_size(factors.totient(n))
    return toti[n]

N = 40*10**6
s = 25
primes = Primes(N)
factors = Factors(N)
total = 0


for i in primes.upto(N):
    if chain_size(i) == s:
        total+=i
print total

