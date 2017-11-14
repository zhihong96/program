# -*- coding: utf-8 -*-

# 优化指数算法,动态规划

#原算法
def maxVal(w, v, i, aW):
    #print 'maxVal called with:', i, aW
    global numCalls
    numCalls += 1
    if i == 0:
        if w[i] <= aW: return v[i]
        else: return 0
    without_i = maxVal(w, v, i-1, aW)
    if w[i] > aW: return without_i
    else: with_i = v[i] + maxVal(w, v, i-1, aW-w[i])
    return max(with_i, without_i)

weights = [1, 5, 3, 4]
values = [15, 10, 9, 5]
numCalls =  0
res = maxVal(weights, values, len(values)-1, 8)
print 'max Val =', res, 'number of calls =', numCalls

weights = [1, 1, 5, 5, 3, 3, 4, 4]
values = [15, 15, 10, 10, 9, 9, 5, 5]
numCalls =  0
res = maxVal(weights, values, len(values)-1, 8)
print 'max Val =', res, 'number of calls =', numCalls

#优化后算法
def fastMaxVal(w, v, i, aW, m):
    global numCalls
    numCalls += 1
    try: return m[(i, aW)]
    except KeyError:
        if i == 0:
            if w[i] <= aW:
               m[(i, aW)] = v[i]
               return v[i]
            else:
                m[(i, aW)] = 0
                return 0
        without_i = fastMaxVal(w, v, i-1, aW, m)
        if w[i] > aW:
            m[(i, aW)] = without_i
            return without_i
        else: with_i = v[i] + fastMaxVal(w, v, i-1, aW-w[i], m)
        res = max(with_i, without_i)
        m[(i, aW)] = res
        return res

def maxVal0(w, v, i, aW):
    m = {}
    return fastMaxVal(w, v, i, aW, m)

weights = [1, 1, 5, 5, 3, 3, 4, 4]
values = [15, 15, 10, 10, 9, 9, 5, 5]
numCalls =  0
res = maxVal0(weights, values, len(values)-1, 8)
print 'max Val =', res, 'number of calls =', numCalls

