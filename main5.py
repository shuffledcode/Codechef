for _ in range(int(input())):
    n,e,h,a,b,c = map(int,input().split())
    minCost = 10**18
    for C in range(n+1):
        if (e<C or h<C):
            break
        maxO = int((e-C)/2)
        maxM = int((h-C)/3)
        if (C+maxO+maxM<n):
            continue
        if (a<b):
            reqO = min(n-C,maxO)
            reqM = n-C-reqO
        else:
            reqM = min(n-C,maxM)
            reqO = n-C-reqM
        cost = a*reqO+b*reqM+c*C
        if (cost<minCost):
            minCost=cost
    if (minCost==10**18):
        print(-1)
    else:
        print(minCost)