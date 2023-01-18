# GraciousQsim
# Author: Grace Unger
# Modified: 1-15-2023

# Basic quantum computer simulator, implementing
# quantum logic gates on a bitwise and statewise level
# 
# All gates are without side effects - we preserve the 
# input and output bits separately. This should probably
# change as the number of bits increases.

import numpy as np
import cmath as cm
from math import pi, sqrt

class Qbit:
    
    # defines a new qbit object a|0> + b|1>
    # Defaults to 1|0> + 0|1>
    def __init__(self, a: complex = complex(1,0), b: complex = complex(0,0)):
        n = abs(a)+abs(b)
        self.a = a/n
        self.b = b/n
        self.idx = 0
        
    #helper method to construct Qbits with binary states
    def lazy(i: bool = False):
        if i: return Qbit.neg(Qbit())
        return Qbit()
                
    def __str__(self):
        return f"{str(self.a)[:6]}|0> + {str(self.b)[:6]}|1>"
    
    def __repr__(self):
        return f"{str(self.a)[:6]}|0> + {str(self.b)[:6]}|1>"
    
    def __iter__(self):
        return self
         
    def __next__(self):
        self.idx += 1
        if self.idx == 1: return self.a
        elif self.idx == 2: return self.b
        else:
            self.idx = 0
            raise StopIteration
        
    # Basic quantum gates:
    def neg(self):
        return Qbit(self.b, self.a)
        
    def swap(self, bit: 'Qbit'):
        return [Qbit(bit.a, bit.b), Qbit(self.a, self.b)]
    
    # input x,y, return x, x^y
    def cnot(self, bit: 'Qbit'):
        return[Qbit(self.a, self.b),
               Qbit(self.a *bit.b+self.b *bit.a,
                    self.a*bit.a+self.b*bit.b)]
        
    def ccnot(self, bita: 'Qbit', bitb: 'Qbit'):
        return[Qbit(bita.a, bita.b), Qbit(bitb.a, bitb.b), 
               Qbit(self.a*bita.a+bitb.a,self.b*bita.b+bitb.b)]
        
    def phase(self):
        return (Qbit(self.a, cm.j * self.b))
    
    def pauliX(self):
        return Qbit(self.b, self.a)
        
    def pauliY(self):
        return Qbit(-cm.j * self.b, cm.j * self.a)
        
    def pauliZ(self):
        return Qbit(self.a, -self.b)
        


# 2^n length state vector, handles operations on complete states instead of
# Individual bits
# Not prioritizing using this yet until I have a better handle on operating
# on the bits themselves
class State:
    
    def __init__(self, bits: list([Qbit])):
        self.stateArray = self.tensor(bits)
        
    # Computes the tensor product of n cubits, 
    # returning a 2^n x 1 state vector 
    def tensor(self, bits: list([Qbit])):
        product = [1]
        for bit in bits:
            product = product * bit.a + product * bit.b
        return product
    
    #CNOT gate
    def cnot(self, state):
        if not len(state) == 4:
            raise Exception(f"{state} length not compatible with CNOT")
        operator = np.matrix([1,0,0,0],[0,1,0,0],[0,0,0,1],[0,0,1,0])
        return np.dot(operator, state)
    
    #Toffoli gate
    def ccnot(self, state):
        if not len(state) == 8: 
                raise Exception(f"{state} length not compatible with TOFF")
        operator = np.matrix([[1,0,0,0,0,0,0,0],[0,1,0,0,0,0,0,0],
                    [0,0,1,0,0,0,0,0],[0,0,0,1,0,0,0,0],
                    [0,0,0,0,1,0,0,0],[0,0,0,0,0,1,0,0],
                    [0,0,0,0,0,0,0,1],[0,0,0,0,0,0,1,0]])
        return np.dot(operator, state)
    
    #SWAP gate; [A,B] -> [B,A]
    def swap(self, state):
        if not len(state) == 4:
            raise Exception(f"{state} length not compatible with SWAP")
        operator = np.matrix([1,0,0,0],[0,0,1,0],[0,1,0,0],[0,0,0,1])
        return np.dot(operator, state)
    
    #NOT gate a|0>+b|1> -> b|0> + a|1>
    def neg(self, state):
        return state[::-1]
    
        