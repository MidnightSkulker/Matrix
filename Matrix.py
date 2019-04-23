#!/usr/local/bin/python3
# This import supports class annotations, e.g. def mulid(self) -> Elem
'''
Haskelle White
Period 3 CSP

parameters: integers, floats, rationals, any number
returns: An evaluated and solved matrix
'''

from __future__ import annotations

# For now, only two-dimensional matrices are represented
# Later we can generalize to n-dimensional matrices
# Infinite dimensional matrices will require some more work :)
# unless we use Haskell :)
class Matrix():
    # The initial representation of the matrix
    matrix = {}

    # Return the dimensions of the matrix
    def dim(self): return self.matrix['dim']
    def rows(self): return self.matrix['dim'][0]
    def cols(self): return self.matrix['dim'][1]

    # Zero filled matrix (Additive identity for matrices)
    def zero(self,dim) -> Matrix:
        for i in range(0, self.rows()):
            for j in range(0, self.cols()):
                zeroMatrix[(i,j)] = 0

    # Initializer for the matrix. It can be initialized by a dictionary
    def __init__ (self, d:dict):
        self.matrix = d
        return

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
        rowz = self.rows()
        colz = self.cols()
        identityMatrix = {'dim':dim}
        # Identity matrix must be a square matrix
        if rowz != colz:
            return None
        # Enter 1 in each diagonal element, and 0 elsewhere
        for i in range(0,colz):
            for j in range(0,rowz):
                # If it is a diagonal element
                if i == j:
                    identityMatrix[(i,j)] = 1
                # Otherwise it is off the diagonal
                else:
                    identityMatrix[(i,j)] = 0
        return Matrix(identityMatrix)

    # Multiply the matrix by another matrix
    def mul(self, b) -> Matrix:
        dima = self.dim()
        dimb = b.dom()
        # Number of columns in a must equal number of rows in b
        if dima[1] != dimb[0]:
            return None
        rows = dima[0]
        cols = dimb[1]
        productMatrix = {'dim':(rows, cols)}
        for i in range(0, rows):
            for j in range(0, cols):
                productMatrix[(i,j)] = 0
                for k in range(0, dima[1]):
                    productMatrix[(i,j)] += self.matrix[(i,k)] * b.access(k,j)
        return Matrix(productMatrix)

    # Add two matrices
    def add(self, b:Matrix) -> Matrix:
        # To add two matrices, they must have the same shape
        if self.dim() != b.dim():
            return None
        sumMatrix = {'dim':(self.rows(), self.cols())}
        for i in range(0, self.rows()):
            for j in range(0, self.cols()):
                sumMatrix[(i,j)] = self.access(i,j) + b.access(i,j)
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
    def access(self, idx):
        return self.matrix[idx]

    # Read in a matrix of the element type
    # The matrix is presented as a dictionary in the input
    def read(self,f) -> Matrix:
        return Matrix(eval(f.read()))

    # Get the nth row of the matrix a, presented as a list
    def getNthRow(self, n):
        rowz = self.rows()
        if n >= rowz or n < 0:
            return None
        # Get a list for the nth row
        rown = []
        for x in self.matrix:
            # Skip the dimension element
            if x == 'dim': continue
            if x[0] == n: rown.append(x)
        return rown

    # Print out an element of the matrix
    def out(self) -> Matrix:
        print('out: ', self.matrix)
        rowz = self.rows()
        for j in range(rowz):
            print(self.getNthRow(j))

testMatrix1 = Matrix({'dim': (2,2), (0,0):7, (0,1):5, (1,0):2, (1,1):4})
testMatrix2 = Matrix({'dim': (2,2), (1,1):4, (0,1):5, (1,0):2, (0,0):7})

testFile = open('test', 'r')

# outMatrix1 = testMatrix1.mul(testMatrix2)
# outMatrix1.out()

