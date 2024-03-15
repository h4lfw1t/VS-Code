'''
Filename:       a8.py
Author:         Patrick Geraghty
Date Created:   2024-03-14
Date Modified:  2024-03-14
Description:    Assignment 8. This program contains functions that perform operations on 2D vectors and matrices.
'''
import numpy as np

def rotation_matrix(theta):
    '''
    (float) -> np.array([[float, float], [float, float]])
    Returns a rotation matrix for a given angle in radians
    Precondition: theta is a float
    '''
    # The rotation matrix is defined as [[cos(theta), -sin(theta)], [sin(theta), cos(theta)]]. Return the numpy array that reflects this.
    return np.array([[np.cos(theta), -np.sin(theta)], [np.sin(theta), np.cos(theta)]])

def vector_rotation(v, theta):
    '''
    (np.array([float, float]), float) -> np.array([float, float])
    Returns a vector rotated by a given angle in radians
    Precondition: v is a 2D np.array, theta is a float
    '''
    # The rotated vector is defined as the dot product of the rotation matrix and the vector. Return the numpy array that reflects this.
    return np.dot(rotation_matrix(theta), v)

def angle_between(v1, v2):
    '''
    (np.array([float, float]), np.array([float, float])) -> float
    Returns the angle between two vectors in radians
    Precondition: v1 and v2 are 2D np.arrays
    '''
    # The angle between two vectors is defined as the arccos of the dot product of the vectors divided by the product of their magnitudes. Return the result of this calculation.
    return np.arccos(np.dot(v1, v2) / (np.linalg.norm(v1) * np.linalg.norm(v2)))

def orthogonal_converter(v1, v2):
    '''
    (np.array([float, float]), np.array([float, float])) -> float
    Returns the angle necessary to rotate v1 to be orthogonal to v2 in radians
    Precondition: v1 and v2 are 2D np.arrays
    '''
    # The angle necessary to rotate v1 to be orthogonal to v2 is defined as the difference between pi/2 and the angle between the vectors. Return the result of this calculation.
    return (np.pi / 2) - angle_between(v1, v2)

def main():
    # Set values for u1 and u2, and calculate the rotation matrix for 45 degrees (pi/4 radians). Print the results.
    r_45 = rotation_matrix(np.pi / 4)
    u1 = np.array([0.9397, 0.342])
    u2 = r_45.dot(u1)
    print(f'r_45: {r_45}')
    print(f'u1: {u1}')
    print(f'u2: {u2}')
    print()
    
    # Calculate the inverse and transpose of r_45, and the matrix multiplication of r_45 by its inverse and transpose. Print the results.
    inverse_r_45 = np.linalg.inv(r_45)
    transposed_r_45 = r_45.T
    print(f'Inverse of r_45: {inverse_r_45}')
    print(f'Transpose of r_45: {transposed_r_45}')
    print()
    
    # Calculate the matrix multiplication of r_45 by its inverse and transpose. Print the results.
    r_45_by_r_45_inverse = np.matmul(r_45, inverse_r_45)
    r_45_by_transposed_r_45 = np.matmul(r_45, transposed_r_45)
    print(f' The matrix multiplication of r_45 by the inverse of r_45 is {r_45_by_r_45_inverse}')
    print(f' The matrix multiplication of r_45 by the transpose of r_45 is {r_45_by_transposed_r_45}')
    print()
    
    # Calculate the matrix multiplication of u2 by the inverse of r_45. Print the results.
    u2_by_r_45_inverse = np.matmul(u2, inverse_r_45)
    print(f' The matrix multiplication of u2 by the inverse of r_45 is {u2_by_r_45_inverse}')
    print()
    
    # Calculate the angle between u2 and u1, and the angle necessary to rotate u1 to be orthogonal to u2. Print the results.
    u3 = np.array([0.6427, 0.766])
    rotation_angle = orthogonal_converter(u2, u3)
    u2_rotated = vector_rotation(u2, rotation_angle)
    print(f'u3: {u3}')
    print(f'Angle between u2 and u3: {angle_between(u2, u3)}')
    print(f'Thus, u3 must be rotated by an angle of {rotation_angle} to be orthogonal to u2, so the rotated u3 is {u2_rotated}')
    # Print the inner product of u3 and the rotated u2, proving that the rotated u2 is indeed orthogonal to u3.
    print(f'The inner product of u3 and the rotated u2 is {np.inner(u3, u2_rotated):.8f}, proving that the rotated u2 is indeed orthogonal to u3.')
    print()
    
    # Calculate the eigenvalues and eigenvectors of the rotation matrix for 0 degrees (0 radians). Print the results.
    r0 = rotation_matrix(0)
    eigenvalues, eigenvectors = np.linalg.eig(r0)
    print(f'Eigenvalues of r0: {eigenvalues}')
    print(f'Eigenvectors of r0: {eigenvectors}')