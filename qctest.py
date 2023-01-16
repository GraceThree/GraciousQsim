# Quantum Computer testing

from qbit import Qbit, State
import numpy as np
import math
from random import uniform

def lazy(i: bool = False):
    if i: return Qbit.neg(Qbit())
    return Qbit()

def cis(theta):
    if theta == math.pi/2: return[0., 1.]
    if theta == 0: return [1., 0.]
    return [math.cos(theta),math.sin(theta)]

[c1,c2,c3,c4] = [uniform(0,2 *math.pi),uniform(0,2 *math.pi),
                 uniform(0,2 *math.pi), uniform(0,2 *math.pi)]

#a,b = Qbit(c1,c2),Qbit(c3,c4)
c = [lazy(0), lazy(1)]
d = [lazy(1), lazy(1)]
print(c,d)
#print(Qbit.swap(a,b))
print(Qbit.swap(c,d))