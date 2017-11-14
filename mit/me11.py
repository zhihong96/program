# -*- coding: utf-8 -*-

def silly():
    res = []
    done = False
    while not done:
        elem=raw_input('enter element. return when done.')
        if elem == '':
            done = True
        else:
            res.append(elem)
    #print 'res should be[1, a, 2]', res
    tmp = res[:]
    #print 'tmp', tmp, 'res', res
    tmp.reverse()
    print 'tmp', tmp, 'res', res
    isPal = (res == tmp)
    #print 'tmp', tmp ,'res', res
    if isPal:
        print 'is a palidrome'
    else:
        print 'is NOT a palidrome'

#if __name__=='__main__':
silly()
