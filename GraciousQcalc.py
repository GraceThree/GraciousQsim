# GraciousQcalc
# Author: Grace Unger
# Modified: 1-15-23

# Basic calculator program running on
# The GraciousQsim quantum computer simulator
from qbit import Qbit, State
import numpy as np
import math
from random import uniform

# Quantum Adder: 
# Input: bit1, bit2, Optional carryIn bit3
# Output: [sum, carry], 
# [bit1+bit2+bit3, bit1*bit2 or bit2*bit3 or bit3* bit1]
def adder(bit1: Qbit, bit2: Qbit, bit3: Qbit = None):
    if not bit3:
        sum = bit1.cnot(bit2)[1]
        carry = bit1.ccnot(bit2, Qbit())
        return [sum, carry]
    sum = bit3.cnot(bit1.cnot(bit2)[1])
    #carry = 

def addbits(num1: list(Qbit), num2: list(Qbit)):
    k = len(num1)
    if not len(num2) == k: raise Exception("Number bit mismatch")
    for i in range(0,k):
        bit1, bit2 = num1[i], num2[i]
        