#!/usr/local/bin/python3
# This import supports class annotations, e.g. def mulid(self) -> Elem
'''
Haskelle White
Period 3 CSP

paramters : integers, floats, rationals, any number
returns: An evaluated and solved matrix
'''

from __future__ import annotations

# An element is a member of a Ring with Identity
# This is a class with addition and multiplication and multiplicative and additive
# identities, which is enough to support matrix multiplication.
class Elem:
    # Multiplicative Identity (e.g. 1 for integers)
    def mulid(self) -> Elem:
        pass
    # Additive Identity (e.g. 0 for integers)
    def addid(self) ->  Elem:
        pass
    # Multiply two elements
    def mul(self, a, b) -> Elem:
        pass
    # Add these two elements
    def add(Elem, a, b) -> Elem:
        pass
    # Read an element from input
    def read(self) -> Elem:
        pass
    # Print out an element
    def out(self,x) -> Elem:
        pass

class IntCRI(Elem):
    def addid(self): return 0
    def mulid(self): return 1
    def mul(self,a,b): return a*b
    def add(self,a,b): return a+b

    def read(self): int(input())
    def out(self,x): print(x)

# For now, only two dimensional matrices are represented
# Later we can generalize to n-dimensional matrices
# Infinite dimensional matrices will require some more work :) unless we use Haskell :)
class Matrix(Elem):
    # Identity matrix (all 1s on the diagonal, zeros elsewhere)
    # This is the multiplicative identity for matrices

    # Representation of the matrix
    # The matrix will be a dictionary of indices with values, like this
    # {'dim':(2,2), (0,0):1, (0,1):2, (1,0):0, (1,1):3}

    # The multiplicative identity for matrices, which is a square matrix that
    # has a 1 on each element of the diagonal, and zero everywhere else.
    # For example, the identity for 2 x 2 matrices is
    # {'dim':(2,2), (0,0):1, (0,1):0, (1,0):0, (1,1):1}
    # Argument dim: A pair specifying the size of the matrix
    # A typical call looks like: id((3,3))
    def id(self,dim) -> Matrix:
        identityMatrix = {'dim':dim}
        rows = dim[0]
        cols = dim[1]
        # Identity matrix must be a square matrix
        if rows != cols:
            return None
        # Enter 1 in each diagonal element, and 0 elsewhere
        for i in range(0,cols):
            for j in range(0,rows):
                # If it is a diagonal element
                if i == j:
                    identityMatrix[(i,j)] = 1
                # Otherwise it is off the diagonal
                else:
                    identityMatrix[(i,j)] = 0
        return identityMatrix
    # Zero filled matrix (Additive identity for matrices)
    def zero(self) -> Matrix:
        pass
    # Multiply two matrices
    def mul(self, a, b) -> Matrix:
        pass
    # Add two matrices
    def add(self, a, b) -> Matrix:
        pass
    # Raise a matrix to an integer power
    def power(self, a, n) -> Matrix:
        pass
    # Access the element at a given set of indices for the matrix
    def access(self, idx) -> Elem:
        pass
    # Read in a matrix of the element type
    def read(self) -> Matrix:
        pass
    # Print out an element of the matrix
    def out(self, a) -> Matrix:
        pass
