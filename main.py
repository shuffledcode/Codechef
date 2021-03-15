import sys
sys.stdin = open('input.txt','r')
sys.stdout = open('output.txt','w')
# for _ in range(int(input())):
n,h,x = map(int,input().split())
lst = list(map(int,input().split()))
if (any(['YES' for i in lst if x+i>=h])): print('YES')
else: print('NO')