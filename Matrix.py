#!/usr/local/bin/python3
# This import supports class annotations, e.g. def mulid(self) -> Elem
'''
Haskelle White
Period 3 CSP

parameters: integers, floats, rationals, any number
returns: An evaluated and solved matrix
'''

from __future__ import annotations

# An element is a member of a Ring with Identity
# This is a class with addition and multiplication and multiplicative
# and additive identities, which is enough to support matrix
# multiplication.
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

# For now, only two-dimensional matrices are represented
# Later we can generalize to n-dimensional matrices
# Infinite dimensional matrices will require some more work :)
# unless we use Haskell :)
class Matrix():
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
    def id(self, dim) -> Matrix:
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
    def zero(self,dim) -> Matrix:
        zeroMatrix = {'dim':dim}
        rows = dim[0]
        cols = dim[1]
        for i in range(0, rows):
            for j in range(0, cols):
                zeroMatrix[(i,j)] = 0

    # Multiply two matrices
    def mul(self, a, b) -> Matrix:
        dima = a['dim']
        dimb = b['dim']
        # Number of columns in a must equal number of rows in b
        if dima[1] != dimb[0]:
            return None
        productMatrix = {'dim':(dima[0], dimb[1])}
        rows = dima[0]
        cols = dimb[1]
        for i in range(0, rows):
            for j in range(0, cols):
                productMatrix[(i,j)] = 0
                for k in range(0, dima[1]):
                    productMatrix[(i,j)] += a[(i,k)] * b[(k,j)]
        return productMatrix

    # Add two matrices
    def add(self, a, b) -> Matrix:
        dima = a['dim']
        dimb = b['dim']
        # To add two matrices, they must have the same shape
        if dima != dimb:
            return None
        sumMatrix = {'dim':(dima, dimb)}
        for i in range(0, dima[0]):
            for j in range(0, dima[1]):
                sumMatrix[(i,j)] = a[(i,j)] + b[(i,j)] # access(b,(i,j))
        return sumMatrix

    # Raise a matrix a to an integer power n
    def power(self, a, n:int) -> Matrix:
        dim = a['dim']
        rows = dim[0]
        cols = dim[1]
        # Can only do powers of a square matrix
        if rows != cols:
            return None
        powerMatrix = id(dim)
        for i in range(0, n):
            powerMatrix = mul(powerMatrix, a)
        return powerMatrix

    # Access the element at a given set of indices for the matrix
    def access(self, a, idx):
        return a[idx]

    # Read in a matrix of the element type
    # The matrix is presented as a dictionary in the input
    def read(self,f) -> Matrix:
        return eval(f.read())

    # Get the nth row of the matrix a, presented as a list
    def getNthRow(self, a, n):
        dima = a['dim']
        rows = dim[0]
        cols = dim[1]
        if n >= rows or n < 0:
            return None
        # Get a list for the nth row
        rown = []
        for x in a:
            if a[0] == n:
                rown.append(x)
        return rown

    # Print out an element of the matrix
    def out(self, a) -> Matrix:
        dima = a['dim']
        rows = dim[0]
        cols = dim[1]
        for j in range(rows):
            rowj = getNthRow9(a,j)
            print(rowj)

testMatrix1 = {'dim': (2,2), (0,0):7, (0,1):5, (1,0):2, (1,1):4}
testMatrix2 = {'dim': (2,2), (1,1):4, (0,1):5, (1,0):2, (0,0):7}

testFile = open('test', 'r')

m = Matrix()
x = m.mul(testMatrix1, testMatrix2)
m.out(x)

