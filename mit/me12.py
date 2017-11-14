# -*- coding: utf-8 -*-

def fib(n):
    global numCalls
    numCalls += 1
    #print 'fib called with', n
    if n == 0 or n == 1: return 1
    if n <= 1:
        return n
    else:
        return fib(n-1) + fib(n-2)
numCalls = 0
#fib(5)

n=30
res = fib(n)
print 'fib of', n, '=', res, 'numCalls =', numCalls

def fastFib(n, memo):
    global numCalls
    numCalls += 1
    #print 'fib1 called with', n
    if not n in memo:
        memo[n] = fastFib(n-1, memo) + fastFib(n-2, memo)
    return memo[n]

def fib1(n):
    memo = {0:1, 1:1}
    return fastFib(n, memo)

numCalls = 0
n = 30
res = fib1(n)
print 'fib of', n, '=', res, 'numCalls=', numCalls


