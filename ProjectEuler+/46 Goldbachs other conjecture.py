import math


def primes(n):
    prime_number = []

    sieve = [True] * (n)

    for p in range(2, n):

        if sieve[p]:
            prime_number.append(p)
            for i in range(p * p, n, p):
                sieve[i] = False
    # print("abc")
    return prime_number[:]


def ways(n):
    count = 0

    pr = primes(n)

    for x in pr:
        dif = n - x
        if ((n-x)/2)%1==0:
            if math.sqrt((n-x)//2) % 1 == 0:
                count += 1
                # print (str(x)+"+ 2 X "+str(int(math.sqrt((n-x)//2))))
    return count

t = int(input())
for _ in range(t):
    print(ways(int(input())))
