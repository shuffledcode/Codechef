import sys
sys.stdin = open('input.txt','r')
sys.stdout = open('output.txt','w')
for _ in range(int(input())): print(len([i for i in input().split('0') if i!='']))