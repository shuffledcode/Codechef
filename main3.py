import sys
sys.stdin = open('input.txt','r')
sys.stdout = open('output.txt','w')
#
for _ in range(int(input())):
    c = bin(int(input()))[2:]
    a = ''
    b = ''
    firstTime=True
    for i in c:
        if i=='0':
            a+='1'
            b+='1'
        else:
            if firstTime:
                a+='1'
                b+='0'
                firstTime=False
            else:
                a+='0'
                b+='1'
    print(int(a,2)*int(b,2))