#!/usr/local/bin/python3
# This import supports class annotations, e.g. def mulid(self) -> Elem
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
    def id(self) -> Matrix:
        pass
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
