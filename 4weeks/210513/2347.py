# -*- coding: utf-8 -*-
"""
Created on Thu May 13 22:50:30 2021

@author: pitit
"""

n, m =map(int, input().split())

a, b= 1, 1
for i in range(n-m+1, n+1):
    a *= i
for i in range(m):
    b *= (m-i)
print(a//b)