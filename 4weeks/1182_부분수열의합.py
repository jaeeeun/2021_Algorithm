# -*- coding: utf-8 -*-
"""
Created on Thu May 13 23:33:01 2021

@author: pitit
"""

from itertools import combinations

N, S = map(int, input().split())

data = list(map(int, input().split()))
cnt = 0
for i in range(N):
    result = list(combinations(data, N-i))
    for j in list(result):
        if sum(j) == S:
            cnt+=1

print(cnt)