# -*- coding: utf-8 -*-
"""
Created on Sat May 15 16:49:00 2021

@author: pitit
"""

import sys
sys.setrecursionlimit(10**8)

def dfs(v, sum1):
    global max_,min_
    if v == N-1:
        if sum1 > max_:
            max_=sum1
        if sum1 < min_:
            min_=sum1
        return
             
    for i in range(4):
        temp = sum1
        if op[i] == 0:
            continue
        elif i == 0:
            sum1 = sum1 + data[v+1]
        elif i == 1:
            sum1 = sum1 - data[v+1]
        elif i == 2:
            sum1 = sum1 * data[v+1]
        elif i == 3:
            sum1 = int(sum1 / data[v+1])
        op[i] -=1
        dfs(v+1,sum1)
        op[i] +=1
        sum1 = temp
        
            
N = int(sys.stdin.readline()) 
data = list(map(int, sys.stdin.readline().split()))
op = list(map(int, sys.stdin.readline().split()))
visit = [0]*N

max_,min_ = -10**8,10**8

dfs(0, data[0])
print(max_)
print(min_)

#print(time.time()-start)


'''
import sys
import time
sys.setrecursionlimit(10**8)

start = time.time()

def dfs(v):
    global max_,min_
    sum1 = data[0]
    str_ = str(data[0])
    if v == N-1:
        j = 1
        for i in range(0, N-1):
            if op3[i] == '+':
                sum1 = sum1 + data[j]
                str_ += '+'
                str_ += str(data[j])
            elif op3[i] == '-':
                sum1 = sum1 - data[j]
                str_ += '-'
                str_ += str(data[j])
            elif op3[i] == '*':
                sum1 = sum1 * data[j]
                str_ += '*'
                str_ += str(data[j])
            elif op3[i] == '/':
                sum1 = int(sum1 / data[j])
                str_ += '/'
                str_ += str(data[j])
            j +=1
        if sum1 > max_:
            max_=sum1
            print(str_,'[',sum1,']')
        if sum1 < min_:
            min_=sum1
        return
        
                
    for i in range(0,N-1):
        if visit[i] == 0:
            op3.append(op[i])
            visit[i] = 1
            dfs(v+1)
            
            op3.pop()
            visit[i] = 0
            
            

            
N = int(input())
#N = int(sys.stdin.readline()) 
#N = int(sys.stdin.readline())


data = list(map(int, input().split()))
op2 = list(map(int, input().split()))

#data = list(map(int, sys.stdin.readline.split()))
#op2 = list(map(int, sys.stdin.readline.split()))
visit = [0]*N

op = []
op3 = []

j , sum1 = 0
max_,min_ = -1,10**8
for i in op2:
    while op2[j] !=0:
        if j == 0:
            op.append('+')
        if j == 1:
            op.append('-')
        if j == 2:
            op.append('*')
        if j == 3:
            op.append('/')
        op2[j] -= 1
    j +=1

dfs(0)
print(max_)
print(min_)

print(time.time()-start)
'''