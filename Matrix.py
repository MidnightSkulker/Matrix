#!/usr/local/bin/python3

'''
Haskelle White
Period 3 CSP

parameters: integers, floats, rationals, any number
returns: An evaluated and solved matrix
'''

# This import supports class annotations, e.g. def mulid(self) -> Elem
from __future__ import annotations

class Matrix():
    # The initial representation of the matrix
    matrix = {}

    # Return the dimensions of the matrix
    def dim(self): return self.matrix['dim']
    def rows(self): return self.matrix['dim'][0]
    def cols(self): return self.matrix['dim'][1]

    # Zero filled matrix (Additive identity for matrices)
    def zero(self,dim) -> Matrix:
        zeroMatrix = { 'dim' : dim }
        for i in range(0, dim[0]):
            for j in range(0, dim[0]):
                zeroMatrix[(i,j)] = 0
        return Matrix(zeroMatrix)

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
    def identity(self, dim) -> Matrix:
        identityMatrix = {'dim':dim}
        # Identity matrix must be a square matrix
        if dim[0] != dim[1]:
            return None
        # Enter 1 in each diagonal element, and 0 elsewhere
        for i in range(0,dim[0]):
            for j in range(0,dim[1]):
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
        dimb = b.dim()
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
                    productMatrix[(i,j)] += self.matrix[(i,k)] * b.access((k,j))
        return Matrix(productMatrix)

    # Add two matrices
    def add(self, b:Matrix) -> Matrix:
        # To add two matrices, they must have the same shape
        if self.dim() != b.dim():
            return None
        sumMatrix = {'dim':(self.rows(), self.cols())}
        for i in range(0, self.rows()):
            for j in range(0, self.cols()):
                sumMatrix[(i,j)] = self.access((i,j)) + b.access((i,j))
        return Matrix(sumMatrix)

    # Subtract two matrices
    def sub(self, b:Matrix) -> Matrix:
        return self.add(b.neg())

    # Negative of matrix
    def neg(self) -> Matrix:
        negMatrix = {'dim':(self.rows(), self.cols())}
        for i in range(0, self.rows()):
            for j in range(0, self.cols()):
                negMatrix[(i,j)] = - self.access((i,j))
        return Matrix(negMatrix)

    # Raise a matrix a to an integer power n
    def power(self, n:int) -> Matrix:
        # Can only do powers of a square matrix
        if self.rows() != self.cols():
            return None
        print('We have a square matrix')
        powerMatrix = self.identity(self.dim())
        powerMatrix.out('powerMatrix.1')
        for i in range(0, n):
            powerMatrix = powerMatrix.mul(self)
        powerMatrix.out('powerMatrix.2')
        return Matrix(powerMatrix)

    # Access the element at a given set of indices for the matrix
    def access(self, idx):
        return self.matrix[idx]

    # Read in a matrix of the element type
    # The matrix is presented as a dictionary in the input
    def read(self,f) -> Matrix:
        return Matrix(eval(f.read()))

    # Get the nth row of the matrix a, presented as a list
    def getNthRow(self, n):
        if n >= self.rows() or n < 0: return None
        # Get a list (rown) for the nth row
        rownidx = []
        # Get the list of keys for the nth row
        for x in self.matrix:
            if x == 'dim': continue # Skip the dimension element
            if x[0] == n: rownidx.append(x)
        rownidx.sort()
        rown = []
        for k in rownidx:
            rown.append(self.access(k))
        return rown

    # Print out an element of the matrix
    def out(self,s) -> Matrix:
        print('raw matrix', s, self.matrix)
        print('matrix', s, 'with dimensions', self.dim())
        rowz = self.rows()
        for j in range(rowz):
            print(self.getNthRow(j))

testMatrix1 = Matrix({'dim': (2,2), (0,0):7, (0,1):5, (1,0):2, (1,1):4})
testMatrix2 = Matrix({'dim': (2,2), (1,1):4, (0,1):5, (1,0):2, (0,0):7})
testMatrix3 = Matrix({'dim': (2,2), (0,0):-2, (0,1):3, (1,0):8, (1,1):0})

testFile = open('test', 'r')

testMatrix1.out('testMatrix1')
testMatrix2.out('testMatrix2')
testMatrix3.out('testMatrix3')
outMatrix1 = testMatrix1.mul(testMatrix2)
outMatrix1.out('outMatrix1 (mul)')
outMatrix2 = testMatrix3.neg()
outMatrix2.out('outMatrix2 (neg)')
outMatrix3 = testMatrix1.add(testMatrix3)
outMatrix3.out('outMatrix3 (add)')
outMatrix4 = testMatrix1.sub(testMatrix3)
outMatrix4.out('outMatrix4 (sub)')
outMatrix5 = testMatrix2.identity((2,2))
outMatrix5.out('outMatrix5 (identity)')
outMatrix6 = outMatrix1.add(outMatrix2)
outMatrix6.out('outMatrix6 (add)')
outMatrix7 = testMatrix1.power(3)
outMatrix7.out('outMatrix7 (power)')
