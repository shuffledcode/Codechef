n,h,x = map(int,input().split())
lst = list(map(int,input().split()))
if (any(['YES' for i in lst if x+i>=h])): print('YES')
else: print('NO')
