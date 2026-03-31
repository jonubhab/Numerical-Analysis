import numpy as np

E=2.220446049250313e-16

def solve(f,a,b):
    global E

    fa,fb=f(a),f(b)

    N=abs(fa-fb)/E
    e=abs(fa-fb)/(1000 if N>1000 else N+1) if a!=b else E

    if abs(a-b)/E<1 or e<E:
        return {(a*abs(fb)+b*abs(fa))/(abs(fa)+abs(fb))}

    x=np.linspace(a,b,(1000 if N>1000 else int(N)))




    y=f(x)
    #start=[a]
    #end=[b]

    roots=set()
    for i in range(len(y)):
        if y[i]==0:
            roots.add(x[i])

    y1=y[:-1]
    y2=y[1:]
    C1=(y1*y2)<0
    for i in range(len(C1)):
        if C1[i]:
            if len(roots)==0 or not x[i] < any(roots) < x[i + 1]:
                roots=roots.union(solve(f,x[i],x[i+1]))

    sgn=np.sign(abs(y)-e)-1
    s1=sgn[:-1]
    s2=sgn[1:]
    C2=(s1*s2)<0
    for i in range(len(C2)):
        if C2[i] and not C1[i]:
            if not x[i] < any(roots) < x[i + 1]:
                roots=roots.union(solve(f,x[i],x[i+1]))

    return roots


def f(x):
    return (x-1)*(x-np.pi)

#print(solve(f,0,10))

