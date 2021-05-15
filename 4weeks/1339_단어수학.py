# -*- coding: utf-8 -*-
"""
Created on Sat May 15 22:25:09 2021

@author: pitit
"""

N = int(input())

alpa = [0] * 26

for i in range(N):
    word = input()
    length = len(word)
    j = 0
    while(length > 0):
        alpa[ord(word[j])-65] += 10**(length-1)
        length -= 1
        j += 1

alpa.sort(reverse=True)
target = 9
res = 0
for i in range(0,26):
    if alpa[i] > 0 :
        res += alpa[i]*target
        target -=1

print(res)

'''''''''''''''''
1. ord함수 
ord(c)는 문자의 유니코드 값을 돌려주는 함수
chr함수와 반대

2. 중요도

3. 참고블로그
https://suri78.tistory.com/183 
'''''''''''''''''