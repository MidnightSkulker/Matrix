#!/usr/local/bin/python3

'''
Haskelle White
Period 3 CSP

parameters: See the method comments
returns: Per method
'''

# This import supports class annotations, e.g. def mulid(self) -> Elem
from __future__ import annotations
import sys

# Strip spaces from each element of a list
def strips(ss):
    newss = []
    for s in ss:
        newss.append(s.strip())
    return(newss)
    
class Matrix():
    # The initial representation of the matrix
    # Representation of the matrix
    # The matrix will be a dictionary of indices with values, like this
    # {(0,0):1, (0,1):2, (1,0):0, (1,1):3}
    nom = "m"
    dimension = (0, 0)
    matrix = {}

    # Return the dimensions of the matrix
    def dim(self): return self.dimension
    def rows(self): return self.dimension[0]
    def cols(self): return self.dimension[1]
    def naym(self): return self.nom

    # Zero filled matrix (Additive identity for matrices)
    def zero(self,dim) -> Matrix:
        zeroMatrix = { 'dim' : dim }
        for i in range(0, dim[0]):
            for j in range(0, dim[1]):
                zeroMatrix[(i,j)] = 0
        return Matrix(zeroMatrix)

    # Initializer for the matrix. It can be initialized by a dictionary
    def __init__ (self, n:str, dim, d:dict):
        self.nom = n
        self.dimension = dim
        for i in range(0, dim[0]):
            for j in range(0, dim[1]):
                if (i,j) in d:
                    self.matrix[(i,j)] = d[(i,j)]
                else:
                    self.matrix[(i,j)] = 0
        self.matrix = d
        return

    # The multiplicative identity for matrices, which is a square matrix that
    # has a 1 on each element of the diagonal, and zero everywhere else.
    # For example, the identity for 2 x 2 matrices is
    # {'dim':(2,2), (0,0):1, (0,1):0, (1,0):0, (1,1):1}
    # Argument dim: A pair specifying the size of the matrix
    # A typical call looks like: id((3,3))
    def identity(self, dim) -> Matrix:
        # Identity matrix must be a square matrix
        if dim[0] != dim[1]:
            return None
        identityMatrix = {}
        # Enter 1 in each diagonal element, and 0 elsewhere
        for i in range(0,dim[0]):
            for j in range(0,dim[1]):
                # If it is a diagonal element
                if i == j:
                    identityMatrix[(i,j)] = 1
                # Otherwise it is off the diagonal
                else:
                    identityMatrix[(i,j)] = 0
        return Matrix('id', dim, identityMatrix)

    # Multiply the matrix by another matrix
    def mul(self, b) -> Matrix:
        dima = self.dim()
        dimb = b.dim()
        # Number of columns in a must equal number of rows in b
        rows = dima[0]
        cols = dimb[1]
        if dima[1] != dimb[0]:
            return None
        productMatrix = {}
        for i in range(0, rows):
            for j in range(0, cols):
                productMatrix[(i,j)] = 0
                for k in range(0, dima[1]):
                    productMatrix[(i,j)] += self.matrix[(i,k)] * b.access((k,j))
        return Matrix(self.naym() + '*' + b.naym(), (rows, cols), productMatrix)

    def cmul(self, c) -> Matrix:
        productMatrix = {}
        for i in range(0, self.rows()):
            for j in range(0, self.cols()):
                productMatrix[(i,j)] = self.matrix[(i,j)] * c
        return Matrix(str(c) + '*' + self.naym(), self.dim(), productMatrix)

    # Add two matrices
    def add(self, b:Matrix) -> Matrix:
        # To add two matrices, they must have the same shape
        if self.dim() != b.dim():
            return None
        sumMatrix = {}
        for i in range(0, self.rows()):
            for j in range(0, self.cols()):
                sumMatrix[(i,j)] = self.access((i,j)) + b.access((i,j))
        return Matrix(self.naym() + '+' + b.naym(), self.dim(), sumMatrix)

    # Negative of matrix
    def neg(self) -> Matrix:
        negMatrix = {}
        for i in range(0, self.rows()):
            for j in range(0, self.cols()):
                negMatrix[(i,j)] = - self.access((i,j))
        return Matrix('(-' + self.nom + ')', self.dim(), negMatrix)

    # Subtract two matrices
    def sub(self, b:Matrix) -> Matrix:
        return self.add(b.neg())

    # Raise a matrix a to an integer power n
    def power(self, n:int) -> Matrix:
        # Can only do powers of a square matrix
        if self.rows() != self.cols():
            return None
        powerMatrix = self.identity(self.dim())
        for i in range(0, n):
            powerMatrix = powerMatrix.mul(self)
        return powerMatrix

    # Access the element at a given set of indices for the matrix
    def access(self, idx):
        return self.matrix[idx]


    # Read in a matrix of the element type
    # The matrix is presented as a dictionary in the input
    def read(self,f) -> Matrix:
        command = f.readline()
        # print('command', command)
        parts = strips(str.split(command, '|'))
        # print('parts', parts)
        if len(parts) == 3:
            nam = parts[0]
            dimm = eval(parts[1])
            arr = eval(parts[2])
        else:
            print('error', command)
        m = Matrix(nam, dimm, arr)
        matrices[nam] = m
        return m

    # Get the nth row of the matrix a, presented as a list
    def getNthRow(self, n):
        if n >= self.rows() or n < 0: return None
        # Get a list (rown) for the nth row
        rownidx = []
        # Get the list of keys for the nth row
        for x in self.matrix:
            if x[0] == n: rownidx.append(x)
        rownidx.sort()
        rown = []
        for k in rownidx:
            rown.append(self.access(k))
        return rown

    # Print out an element of the matrix
    def out(self) -> Matrix:
        # print('raw matrix', s, self.matrix)
        print('matrix', self.nom , 'with dimensions', self.dim())
        rowz = self.rows()
        for j in range(rowz):
            print(self.getNthRow(j))

# The global collection of matrices input or created by the user
matrices = {}

def isConst(s) -> bool:
    try:
        return type(eval(s)) is int
    except:
        return False

# _ for negate
# ! for new matrix
# | for separating fields
operators = ['+', '-', '*', '^', '_', '!']
def isOperator(s) -> bool: return s in operators
def command(com:str) -> Matrix:
    # Here is a typical command, in this case to create a new matrix called 'm1'
    # ! {'name':'m2', 'dim':(2,2), (1,1):4, (0,1):5, (1,0):2, (0,0):8}
    # It is a 2 x 2 matrix, with the entries listed above.
    # The operator is the first character, so op (below) will be '!'
    op = com[0]
    # com will be the rest of the command, after the operator and the space
    # So for the create command above, date will be the string:
    # "{'name':'m2', 'dim':(2,2), (1,1):4, (0,1):5, (1,0):2, (0,0):8}"
    data = com[2:]
    # Now handle each different operation separately.
    if isOperator(op):
        if op == '+': # Addition operator
            # Split the data at the spaces. For the command:
            # + o1 m3 o2
            # operands will be ['o1', 'm3', 'o2']
            operands = str.split(data)
            # Now get each operand. For our example operand0 will be 'o1',
            # operand1 will be 'm3', and operand2 will be 'o2'.
            # operand0 will the the *matrix* o1, looked up in the list of
            # existing matrices.
            operand0 = matrices[operands[0]]
            # operand1 will be the *matrix* m3, looked up in the list of
            # existing matrices.
            operand1 = matrices[operands[1]]
            # operand2 will be just the *string* 'o2', naming a matrix to be
            # created.
            operand2 = operands[2]
            # Perform the operation, which creates a new matrix in the
            # outMatrix variable.
            outMatrix = operand0.add(operand1)
            # Store the new matrix under the name 'o2' (in our example)
            matrices[operand2] = outMatrix
            # Return the freshly created matrix.
            return outMatrix
        elif op == '-': # Difference operator
            operands = str.split(data)
            operand0 = matrices[operands[0]]
            operand1 = matrices[operands[1]]
            operand2 = operands[2]
            outMatrix = operand0.sub(operand1)
            matrices[operand2] = outMatrix
            return outMatrix
        elif op == '*': # Multiplication operator
            operands = str.split(data)
            operand0 = matrices[operands[0]]
            operand1 = matrices[operands[1]]
            operand2 = operands[2]
            outMatrix = operand0.mul(operand1)
            matrices[operand2] = outMatrix
            return outMatrix
        elif op == '^': # Power operator
            operands = str.split(data)
            operand0 = matrices[operands[0]]
            operand1 = operands[1]
            operand2 = operands[2]
            outMatrix = operand0.power(int(operand1))
            matrices[operand2] = outMatrix
            return outMatrix
        elif op == '_': # Negation operator
            operands = str.split(data)
            operand0 = matrices[operands[0]]
            operand1 = operands[1]
            outMatrix = operand0.neg()
            matrices[operand1] = outMatrix
            return outMatrix
        elif op == '!': # New matrix operator
            inputMatrix = eval(data)
            nom = inputMatrix['name']
            dimm = inputMatrix['dim']
            del inputMatrix['name']
            del inputMatrix['dim']
            out = Matrix(nom, dimm, inputMatrix)
            matrices[nom] = out
            return out
        else:
            sys.exit('operator' + op + 'is invalid')
    else:
        print('Invalid operation', op)

def script(f:str):
    fhandle = open(f, 'r')
    done = False
    while not done:
        line = fhandle.readline()
        if len(line) == 0:
            break
        print('Executing line:', line)
        res = command(line)
        res.out()
        input()
    fhandle.close()
    
#------------------------------------------------------------------------------
# Test Data
#------------------------------------------------------------------------------
# testMatrix1 = Matrix('testMatrix1', (2,2), {(0,0):7, (0,1):5, (1,0):2, (1,1):4})
# testMatrix2 = Matrix('testMatrix2', (2,2), {(1,1):4, (0,1):5, (1,0):2, (0,0):7})
# testMatrix3 = Matrix('testMatrix3', (2,2), {(0,0):-2, (0,1):3, (1,0):8, (1,1):0})

# testMatrix1.out()
# testMatrix2.out()
# testMatrix3.out()

# #------------------------------------------------------------------------------
# # Test Operations
# #------------------------------------------------------------------------------
# outMatrix1 = testMatrix1.mul(testMatrix2)
# outMatrix1.out()
# outMatrix2 = testMatrix3.neg()
# outMatrix2.out()
# outMatrix3 = testMatrix1.add(testMatrix3)
# outMatrix3.out()
# outMatrix4 = testMatrix1.sub(testMatrix3)
# outMatrix4.out()
# outMatrix5 = testMatrix2.identity((2,2))
# outMatrix5.out()
# outMatrix6 = outMatrix1.add(outMatrix2)
# outMatrix6.out()
# outMatrix7 = testMatrix1.power(3)
# outMatrix7.out()
# outMatrix8 = outMatrix7.cmul(4)
# outMatrix8.out()

# dummy = Matrix('dummy',(0,0), {})
# dummy.out ()

testFile = open('test', 'r')
# # m1 = dummy.read(testFile)
# # m1 .out()
l1 = testFile.readline()
l2 = testFile.readline()
l3 = testFile.readline()
l4 = testFile.readline()
l5 = testFile.readline()
l6 = testFile.readline()
l7 = testFile.readline()
