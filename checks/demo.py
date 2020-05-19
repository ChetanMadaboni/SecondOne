# -*- coding: utf-8 -*-
"""
Created on Sun Apr 19 05:39:34 2020

@author: HP
"""

if __name__ == '__main__':
    n=input()
    r=[]
    for i in n[len(n)::-1]:
        r.append(i)
    st="".join(str(x) for x in r)
    print(st)
print("changed statement")        
