# -*- coding: utf-8 -*-
"""
Created on Thu May 13 22:50:30 2021

@author: pitit
"""

"""""""""""""""""""""""
* Source(21.05.13)
"""""""""""""""""""""""
n, m =map(int, input().split())
a, b= 1, 1
for i in range(n-m+1, n+1):
    a *= i
for i in range(m):
    b *= (m-i)
print(a//b)

"""""""""""""""""""""""
* Bug1 (21.05.13 23:24)
    print(int(a/b)) -> a/b를 하면 float 형으로 바껴서 결과값이 달라졌음
    test case:
        100 50

"""""""""""""""""""""""

""""""""""""""""""""""
* Ohter's Source

import math

n, m = map(int, input().split())
up = math.factorial(n)
down = (math.factorial(n - m)) * (math.factorial(m))
print(up // down)
""""""""""""""""""""""