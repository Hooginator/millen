#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep  2 17:38:58 2018

@author: hoog
"""

import numpy as np
import matplotlib.pyplot as plt

def cMult(a,b):
    # Complex NUmbers Multiplication
    return [a[0]*b[0]-a[1]*b[1],a[0]*b[1]+a[1]*b[0]]




def zeta(s,inf=20):
    # Riemann Zeta Function
    re,im = [0],[0]
    for n in range(inf):
        mag = 1/(n+1)**s[0]
        re.append(re[n]+mag*np.cos(np.log(1/(n+1))*s[1]))
        im.append(im[n]+mag*np.sin(np.log(1/(n+1))*s[1]))
    return [re,im]
    
    

[re,im] = zeta((1.4,1.1))

plt.plot(re,im,lw=1)
plt.scatter(re,im,c = range(len(re)))