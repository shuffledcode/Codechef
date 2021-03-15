# n = int(input())
# n, k = map(int, input().split())
# s = input()
# l = list(map(int, input().split()))

from math import *
from collections import *
import sys

sys.setrecursionlimit(10 ** 9)

def panda(n, e, h, a, b, c, cnt):
    c1 = (h - n) // 2
    c2 = (3 * n - h + 2) // 3
    # print(c1, c2)
    if n <= 0:
        return 0

    if 3 * n <= h:
        #print(1)
        cnt = min(cnt, n * b)

    if n <= e and n <= h:
        #print(2)
        cnt = min(cnt, n * c)

    if 2 * n <= e:
        #print(3)
        cnt = min(cnt, n * a)

    if e - n >= 1 and e - n >= n - h:
        #print(4)
        if a < c:
            x1 = min(n - 1, e - n)
        else:
            x1 = max(1, n - h)
        cnt = min(cnt, (a - c) * x1 + n * c)

    if c1 >= 1 and c1 >= n - e:
        #print(5)
        if b < c:
            x1 = min(n - 1, c1)
        else:
            x1 = max(1, n - e)
        cnt = min(cnt, (b - c) * x1 + n * c)

    if e // 2 >= 1 and e // 2 >= c2:
        #print(6)
        if a < b:
            x1 = min(n - 1, e // 2)
        else:
            x1 = max(1, c2)
        cnt = min(cnt, (a - b) * x1 + n * b)

    if cnt == inf:
        return -1

    if e >= 3 and h >= 4 and n >= 3:
        # print(7)
        cnt = min(cnt, a + b + c + panda(n - 3, e - 3, h - 4, a, b, c, cnt))

    return cnt


# t = 1
t = int(input())
for _ in range(t):
    n, e, h, a, b, c = map(int, input().split())
    print(panda(n, e, h, a, b, c, inf))

