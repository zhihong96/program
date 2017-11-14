# -*- coding: utf-8 -*-

def squareRootNR(x, epsilon):
    """Assumes x >= 0 and epsilon > 0
        Return y s.t. y*y is within epsilon of x"""
    assert x >= 0, 'x must be non-negative, not' + str(x)
    assert epsilon > 0, 'epsilon must be positive, not' + str(epsilon)
    x = float(x)
    guess = x/2.0
    guess = 0.001
    diff = guess**2 - x
    ctr = 1
    while abs(diff) > epsilon and ctr <= 100:
        #print 'Error:', diff, 'guess:', guess
        guess = guess - diff/(2.0*guess)
        diff = guess**2 - x
        ctr += 1
    assert ctr <= 100, 'Iteration count exceeded'
    print 'NR method. Num. iterations:', ctr, 'Estimate:', guess
    return guess

squareRootNR(4,0.001)
squareRootNR(9,0.0001)
squareRootNR(10000,0.0001)
