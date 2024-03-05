'''
Filename:       lab8.py
Author:         Patrick Geraghty
Date Created:   2024-03-05
Date Modified:  2024-03-05
Description:    Lab 8
'''

import numpy as np

# Part 1
print('Part 1: \n')                         # Print Part 1

# a) 3x + 2y = 3, 3x - 6y = 6
a_coeff = np.array([[-3, 2], [3, -6]])      # Matrix of coefficients
a_const = np.array([3, 6])                  # Matrix of constants
a = np.linalg.solve(a_coeff, a_const)       # Solve the system of equations
print('a) ', a, end='\n\n')                 # Print the solution

# b) 2a + 7c + 4d + 2e = 7, 4a - 6b - 6c + 4d -6e = 7, 7b - 7c - 2d + 8e = 1, a - 8c - 3d - 6e = -7, -a + 8b + 6c = 6
b_coeff = np.array([[2, 0, 7, 4, 2], [4, -6, -6, 4, -6], [0, 7, -7, -2, 8], [1, 0, -8, -3, -6], [-1, 8, 6, 0, 0]])      # Matrix of coefficients
b_const = np.array([7, 7, 1, -7, 6])                                                                                    # Matrix of constants   
b = np.linalg.solve(b_coeff, b_const)                                                                                   # Solve the system of equations
print('b) ', b, end='\n\n')

# c) -5a + (1 - 2j)b + 7c = 4 - 4j, 3a + (1 + 2j)b - (1 + 7j)c = 9 + 3j, -7a - (1 + 7j)b - (3 + 9j)c = -9
c_coeff = np.array([[-5, 1 - 2j, 7], [3, 1 + 2j, -1 - 7j], [-7, -1 + 7j, -3 + 9j]])     # Matrix of coefficients
c_const = np.array([4 - 4j, 9 + 3j, -9])                                                # Matrix of constants
c = np.linalg.solve(c_coeff, c_const)                                                   # Solve the system of equations
print('c) ', c, end='\n\n')

# Part 2
print('Part 2: \n')                                                                                     # Print Part 2

# a) A = [[0, 3, 3], [5, 5, -4], [5, -4, 5]]
A = np.array([[0, 3, 3], [5, 5, -4], [5, -4, 5]])                                                       # Define matrix A
a_eigenvalues, a_eigenvectors = np.linalg.eig(A)                                                        # Calculate eigenvalues and eigenvectors
print('a) \nEigenvalues: \n', a_eigenvalues, '\nEigenvectors: \n', a_eigenvectors, end='\n\n')                 # Print the eigenvalues and eigenvectors
# Check if eigenvectors are orthogonal
for i in range(len(a_eigenvectors)):                                                                    # Iterate through the eigenvectors
    for j in range(i+1, len(a_eigenvectors)):
        dot_product = np.vdot(a_eigenvectors[:, i], a_eigenvectors[:, j])                                # Calculate the dot product of the eigenvectors at [i] and [j]
        if np.isclose(dot_product, 0):                                                                  # If the dot product is close to 0, the eigenvectors are orthogonal
            print(f"Eigenvectors {np.round(a_eigenvectors[i], 3)} and {np.round(a_eigenvectors[j], 3)} are orthogonal.")
        else:                                                                                           # If the dot product is not close to 0, the eigenvectors are not orthogonal
            print(f"Eigenvectors {np.round(a_eigenvectors[i], 3)} and {np.round(a_eigenvectors[j], 3)} are not orthogonal.")
print()                                                                                                 # Round to 3 decimal places for readability

# b) B = [[3, 1 - 2j, 3 - 4j], [1 + 2j, -4, -2 + 1j], [3 + 4j, -2 - 1j, -3]]
B = np.array([[3, 1 - 2j, 3 - 4j], [1 + 2j, -4, -2 + 1j], [3 + 4j, -2 - 1j, -3]])                       # Define matrix B
b_eigenvalues, b_eigenvectors = np.linalg.eig(B)                                                        # Calculate eigenvalues and eigenvectors
print('b) \nEigenvalues: \n', b_eigenvalues, '\nEigenvectors: \n', b_eigenvectors, end='\n\n')                 # Print the eigenvalues and eigenvectors
# Check if eigenvectors are orthogonal
for i in range(len(b_eigenvectors)):                                                                    # Iterate through the eigenvectors
    for j in range(i+1, len(b_eigenvectors)):
        dot_product = np.vdot(b_eigenvectors[:, i], b_eigenvectors[:, j])                                # Calculate the dot product of the eigenvectors at [i] and [j]
        if np.isclose(dot_product, 0):                                                                  # If the dot product is close to 0, the eigenvectors are orthogonal
            print(f"Eigenvectors {np.round(b_eigenvectors[i], 3)} and {np.round(b_eigenvectors[j], 3)} are orthogonal.")          
        else:                                                                                           # If the dot product is not close to 0, the eigenvectors are not orthogonal
            print(f"Eigenvectors {np.round(b_eigenvectors[i], 3)} and {np.round(b_eigenvectors[j], 3)} are not orthogonal.")
print()                                                                                                 # Round to 3 decimal places for readability

# Part 3
print('Part 3: \n')                                                             # Print Part 3

# a) D = [[-5, 1 - 2j, 7], [3, 1 + 2j, -1 - 7j], [-7, -1 + 7j, -3 + 9j]]
D = np.array([[-5, 1 - 2j, 7], [3, 1 + 2j, -1 - 7j], [-7, -1 + 7j, -3 + 9j]])   # Define matrix D
D_h = D.conj().T                                                                # Calculate the Hermitian of matrix D
print('a) \nD: \n', D, '\nD_h: \n', D_h, end='\n\n')                            # Print D and its Hermitian matrix
if np.array_equal(D, D_h):                                                      # Check if D is Hermitian
    print('D is Hermitian.')
else:
    print('D is not Hermitian.')
print()

# b) E = 
E = np.array([[5, 5 + 3j, -5j], [5 - 3j, 2, 5], [5j, 5, 3]])                    # Define matrix E
E_h = E.conj().T                                                                # Calculate the Hermitian of matrix E
print('b) \nE: \n', E, '\nE_h: \n', E_h, end='\n\n')                            # Print E and its Hermetian matrix
if np.array_equal(E, E_h):                                                      # Check if E is Hermitian
    print('E is Hermitian.')
else:
    print('E is not Hermitian.')
print()

# c) F =
F = np.array([[3, 1 - 2j, 3 - 4j], [1 + 2j, -4, -2 + 1j], [3 + 4j, -2 - 1j, -3]])   # Define matrix F
F_h = F.conj().T                                                                    # Calculate the Hermitian of matrix F
print('c) \nF: \n', F, '\nF_h: \n', F_h, end='\n\n')                                # Print F and its Hermetian matrix
if np.array_equal(F, F_h):                                                          # Check if F is Hermitian
    print('F is Hermitian.')
else:
    print('F is not Hermitian.')
print()
