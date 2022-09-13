# Python program for Matrix Addition using numpy
import numpy as np
def add_matrix(a,b):
    # Check if the matrices are of same order
    if a.shape==b.shape:
        print("The sum of the two matrices is")
        print(a+b)
    else:
        print("The matrices are of different order")

# Subtraction of two matrices
def sub_matrix(a,b):
    if(a.shape==b.shape):
        print("The difference of the two matrices is")
        print(a-b)
    else:
        print("The matrices are of different order")

# Scalar multiplication of a matrix
def scalar_matrix(a):
    print("The matrix is")
    print(a)
    print("Enter the scalar value")
    s=int(input())
    print("The product of the matrix and scalar is")
    print(s*a)

# Element wise multiplication of two matrices
def element_matrix(a,b):
    if(a.shape==b.shape):
        print("The element wise product of the two matrices is")
        print(a*b)
    else:
        print("The matrices are of different order")

# Matrix multiplication of two matrices
def matrix_matrix(a,b):
    if(a.shape[1]==b.shape[0]):
        print("The product of the two matrices is")
        print(np.matmul(a,b))
    else:
        print("The matrices are of different order")

# Transpose of a matrix
def transpose_matrix(a):
    print("The transpose of the matrix is")
    print(a.transpose())

# Trace of a matrix
def trace_matrix(a):
    # Check if the matrix is a square matrix
    if(a.shape[0]==a.shape[1]):
        print("The trace of the matrix is")
        print(np.trace(a))
    else:
        print("The matrix is not a square matrix")

#Solving a system of linear equations
def linear_matrix(a,b):
    # Check if the matrix is a square matrix
    if(a.shape[0]==a.shape[1]):
        print("The solution of the system of linear equations is")
        print(np.linalg.solve(a,b))
    else:
        print("The matrix is not a square matrix")

# Determinant of a matrix
def determinant_matrix(a):
    # Check if the matrix is a square matrix
    if(a.shape[0]==a.shape[1]):
        print("The determinant of the matrix is")
        print(np.linalg.det(a))
    else:
        print("The matrix is not a square matrix")

# Inverse of a matrix
def inverse_matrix(a):
    # Check if the matrix is a square matrix
    if(a.shape[0]==a.shape[1]):
        print("The inverse of the matrix is")
        print(np.linalg.inv(a))
    else:
        print("The matrix is not a square matrix")

#Single value decomposition of a matrix
def svd_matrix(a):
    print("The single value decomposition of the matrix is")
    print(np.linalg.svd(a))
#
# Driver code
if __name__ == "__main__":
    print("Enter the number of rows and columns of the first matrix")
    m = int(input())
    n = int(input())
    print("Enter the elements of the first matrix")
    a = np.array([[int(input()) for i in range(n)] for j in range(m)])
    # print("Enter the number of rows and columns of the second matrix")
    # p = int(input())
    # q = int(input())
    # print("Enter the elements of the second matrix")
    # b = np.array([[int(input()) for i in range(q)] for j in range(p)])
    print("The first matrix is")
    print(a)
    # print("The second matrix is")
    # print(b)
    # add_matrix(a,b)
    # sub_matrix(a,b)
    # scalar_matrix(a)
    # element_matrix(a,b)
    # matrix_matrix(a,b)
    # transpose_matrix(a)
    trace_matrix(a)