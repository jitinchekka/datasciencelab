# Python program for Matrix Addition using numpy
import numpy as np


def add_matrix(a, b):
    # Check if the matrices are of same order
    if a.shape == b.shape:
        print("The sum of the two matrices is")
        print(a + b)
    else:
        print("The matrices are of different order")


# Subtraction of two matrices


def sub_matrix(a, b):
    if a.shape == b.shape:
        print("The difference of the two matrices is")
        print(a - b)
    else:
        print("The matrices are of different order")


# Scalar multiplication of a matrix


def scalar_matrix(a):
    print("The matrix is")
    print(a)
    print("Enter the scalar value")
    s = int(input())
    print("The product of the matrix and scalar is")
    print(s * a)


# Element wise multiplication of two matrices


def element_matrix(a, b):
    if a.shape == b.shape:
        print("The element wise product of the two matrices is")
        print(a * b)
    else:
        print("The matrices are of different order")


# Matrix multiplication of two matrices


def matrix_matrix(a, b):
    if a.shape[1] == b.shape[0]:
        print("The product of the two matrices is")
        print(np.matmul(a, b))
    else:
        print("The matrices are of different order")


# Transpose of a matrix


def transpose_matrix(a):
    print("The transpose of the matrix is")
    print(a.transpose())


# Trace of a matrix


def trace_matrix(a):
    # Check if the matrix is a square matrix
    if a.shape[0] == a.shape[1]:
        print("The trace of the matrix is")
        print(np.trace(a))
    else:
        print("The matrix is not a square matrix")


# Solving a system of linear equations


def linear_matrix(a, b):
    # Check if the matrix is a square matrix
    if a.shape[0] == a.shape[1] and a.shape[0] == b.shape[0] and b.shape[1] == 1:
        try:
            print("The solution of the linear equation is")
            print(np.linalg.solve(a, b))
        except np.linalg.LinAlgError:
            print("Error;The matrix is singular")
    else:
        print("The matrix is not a square matrix")


# Determinant of a matrix


def determinant_matrix(a):
    # Check if the matrix is a square matrix
    if a.shape[0] == a.shape[1]:
        print("The determinant of the matrix is")
        print(np.linalg.det(a))
    else:
        print("The matrix is not a square matrix")


# Inverse of a matrix


def inverse_matrix(a):
    # Check if the matrix is a square matrix
    if a.shape[0] == a.shape[1]:
        print("The inverse of the matrix is")
        print(np.linalg.inv(a))
    else:
        print("The matrix is not a square matrix")


# Single value decomposition of a matrix


def svd_matrix(a):
    print("The single value decomposition of the matrix is")
    print(np.linalg.svd(a))


# Eigen value
def eigen_matrix(a):
    print("The eigen values of the matrix is")
    print(np.linalg.eig(a))


# Search for a value in a matrix


def search_matrix(a):
    print("The matrix is")
    print(a)
    print("Enter the value to be searched")
    s = int(input())
    print("The position of the value is")
    print(np.where(a == s))


# Differnce of sum of upper and lower triangular matrix


def diff_matrix(a):
    print("The matrix is")
    print(a)
    upper_sum = 0
    lower_sum = 0
    for i in range(0, a.shape[0]):
        for j in range(0, a.shape[1]):
            if i > j:
                lower_sum += a[i][j]
            elif i < j:
                upper_sum += a[i][j]
    print("The difference of sum of upper and lower triangular matrix is")
    print(upper_sum - lower_sum)


# Driver code
if __name__ == "__main__":
    print("Enter the number of rows and columns of the first matrix")
    m = int(input())
    n = int(input())
    print("Enter the elements of the first matrix")
    a = np.array([[int(input()) for i in range(n)] for j in range(m)])
    print("Enter the number of rows and columns of the second matrix")
    p = int(input())
    q = int(input())
    print("Enter the elements of the second matrix")
    b = np.array([[int(input()) for i in range(q)] for j in range(p)])
    print("The first matrix is")
    print(a)
    print("The second matrix is")
    print(b)
    # Menu driven program
    while True:
        print("Enter your choice")
        print("1.Addition of two matrices")
        print("2.Subtraction of two matrices")
        print("3.Scalar multiplication of a matrix")
        print("4.Element wise multiplication of two matrices")
        print("5.Matrix multiplication of two matrices")
        print("6.Transpose of a matrix")
        print("7.Trace of a matrix")
        print("8.Solving a system of linear equations")
        print("9.Determinant of a matrix")
        print("10.Inverse of a matrix")
        print("11.Single value decomposition of a matrix")
        print("12.Eigen value")
        print("13.Search for a value in a matrix")
        print("14.Differnce of sum of upper and lower triangular matrix")
        print("15.Exit")
        ch = int(input())
        if ch == 1:
            add_matrix(a, b)
        elif ch == 2:
            sub_matrix(a, b)
        elif ch == 3:
            scalar_matrix(a)
        elif ch == 4:
            element_matrix(a, b)
        elif ch == 5:
            matrix_matrix(a, b)
        elif ch == 6:
            transpose_matrix(a)
        elif ch == 7:
            trace_matrix(a)
        elif ch == 8:
            linear_matrix(a, b)
        elif ch == 9:
            determinant_matrix(a)
        elif ch == 10:
            inverse_matrix(a)
        elif ch == 11:
            svd_matrix(a)
        elif ch == 12:
            eigen_matrix(a)
        elif ch == 13:
            search_matrix(a)
        elif ch == 14:
            diff_matrix(a)
        elif ch == 15:
            break
        else:
            print("Invalid choice")
