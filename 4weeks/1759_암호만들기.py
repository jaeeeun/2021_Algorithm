# -*- coding: utf-8 -*-
"""
Created on Sat May 15 19:03:13 2021

@author: pitit
"""
def vowel(char):
    if char == 'a' or char == 'e' or char == 'i' or char == 'o' or char == 'u':
        return 1
    else:
        return 0

def consonat(char):
    if char == 'a' or char == 'e' or char == 'i' or char == 'o' or char == 'u':
        return 0
    else:
        return 1
    
def dfs(index, point, vow, cons): #인덱스, 모음, 자음
    if index == L:
        if vow >=1 and cons >=2:
            for i in res:
                print(i, end='')
            print()
        return
                    
    for i in range(point, len(alpa)):
        res.append(alpa[i])
        dfs(index+1, i+1, vow+vowel(alpa[i]), cons+consonat(alpa[i]))
        res.pop()

        
L, C = map(int, input().split())
alpa = list(map(str, input().split()))
res = []

alpa.sort()
dfs(0,0,0,0)
