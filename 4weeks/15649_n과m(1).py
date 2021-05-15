# -*- coding: utf-8 -*-
"""
Created on Sat May 15 14:53:53 2021

@author: pitit
"""

def dfs(v):
    
    if v == M:
        for i in range(0, M):
            print(data[i],end=' ')
        print()
        
    for i in range(0,N):
        if visit[i] == 0:
            data.append(i+1)
            visit[i] = 1
            dfs(v+1)
            
            data.pop()
            visit[i] = 0

            
N, M = map(int, input().split())

data = []
visit = [0] * (N+1)

dfs(0)
