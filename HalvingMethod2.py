#halving method

import matplotlib.pyplot as plt
import numpy as np

def halving(l,r,e,ap,bp,cp):
    l_domain=l 
    r_domain=r
    x=0
    coeff=[ap,bp,cp]
    epsilon = e
    a=l_domain
    b=r_domain
    iteration=0
    length = (b-a)
    
    x1=l_domain
    x2=r_domain
    fxlist=[x**2,x**1,x**0] #your unimodal equation here
    xplot = np.arange(l, r, e)
    aplot = ap
    bplot = bp
    cplot = cp
    yplot = aplot*(xplot**2) + bplot*xplot + cplot 
    plt.plot(xplot,yplot)
    def fx(fn):
        Y=0
        for i in range(len(coeff)):
            Y=Y+(fn[i]*coeff[i])
        return Y
    print("This is running!")
    while epsilon<length:
        iteration=iteration+1
        print("Length:",length)
        oldx1=x1
        oldx2=x2
        x1= a+(length/16)
        x2= b-(length/16)
        print("X1:",x1)
        print("X2:",x2)
        x=x1
        fxlist=[x**2,x**1,x**0]
        f1=fx(fxlist)
        x=x2
        fxlist=[x**2,x**1,x**0]
        print("f1:",f1)
        x=x2
        f2=fx(fxlist)
        print("f2:",f2)

        if(f1>f2):
            a=x1
            b=oldx2
        else:
            b=x2
            a=oldx1
        
        plt.plot(a,f1,'bo')
        plt.plot(b,f2,'yo')
        length=(b-a)
        print("length:",length)
        print("a:",a)
        print("b:",b) 
    
        print("---------------------")    
    print("Iterations:",iteration)
    x = (a+b)/2
    print("minimal x:",x)
    minimia=fx(fxlist)
    print("minima:",minimia)
    plt.plot(x,minimia,'ro')
    plt.show()



    

halving(1,5,0.9,1,128,0)



