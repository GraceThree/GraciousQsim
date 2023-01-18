# GraciousQcalc-Bitwise
# Author: Grace Unger
# Modified: 1-15-23

# Basic calculator program running on
# The GraciousQsim quantum computer simulator
# Circuits\algs my own, I don't know whether they're standard
# or very strange :)
from qbit import Qbit, State
import numpy as np
import math
from random import uniform

# Quantum Adder: 
# Input: bit1, bit2, Optional carryIn bit3
# Output: [sum, carry], 
# [bit1+bit2+bit3, bit1*bit2 or bit2*bit3 or bit3* bit1]
# Follows the no side effects convention, probably not permanent
def adder(bit1: Qbit, bit2: Qbit, bit3: Qbit = None):
    if not bit3:
        sum = bit1.cnot(bit2)[1]
        carry = bit1.ccnot(bit2, Qbit())[2]
        return [sum, carry]
    sum = bit3.cnot(bit1.cnot(bit2)[1])[1]
    temp = cccnot(bit1, bit2, bit3, bit3.ccnot( bit1, bit2)[2])[3]
    carry = cccnot(bit1, bit2, Qbit.neg(bit3),temp)[3]
    return [sum, carry]
    
# This seems like it might be better to implement locally until
# I figure out how to do a generalized control gates bitwise
# bit4 is the mutated bit. When this gets implemented into 
# Qbit proper, self will be the modified bit as in cnot/ccnot
def cccnot(bit1: Qbit, bit2: Qbit, bit3: Qbit, bit4: Qbit):
    return [Qbit(bit1.a, bit1.b), 
            Qbit(bit2.a, bit2.b), 
            Qbit(bit3.a, bit3.b),
            Qbit(bit1.a*bit2.a*bit3.a+bit4.a,bit1.b*bit2.b*bit3.b+bit4.b)]

def addbits(num1: list([Qbit]), num2: list([Qbit])):
    k = len(num1)
    sum = []
    if not len(num2) == k: raise Exception("Number bit mismatch")
    carry = Qbit()
    for i in range(0,k):
        bit1, bit2 = num1[i], num2[i]
        [temp, carry] = adder(bit1, bit2, carry)
        sum+=[temp]
    return sum+[carry]

a = [0,1,1,0,1]
b = [1,0,1,0,1]
abits = [Qbit.lazy(i) for i in a]
bbits = [Qbit.lazy(i) for i in b]
s1 = State(abits)
s2 = State(bbits)

print(addbits(abits, bbits))