'''
Filename:       a8.py
Author:         Patrick Geraghty
Date Created:   2024-03-14
Date Modified:  2024-03-14
Description:    Assignment 8
'''
import numpy as np

def rotation_matrix(theta):
    '''
    (float) -> np.array([[float, float], [float, float]])
    Returns a rotation matrix for a given angle in radians
    Precondition: theta is a float
    '''
    return np.array([[np.cos(theta), -np.sin(theta)], [np.sin(theta), np.cos(theta)]])

def vector_rotation(v, theta):
    '''
    (np.array([float, float]), float) -> np.array([float, float])
    Returns a vector rotated by a given angle in radians
    Precondition: v is a 2D np.array, theta is a float
    '''
    return np.dot(rotation_matrix(theta), v)

def angle_between(v1, v2):
    '''
    (np.array([float, float]), np.array([float, float])) -> float
    Returns the angle between two vectors in radians
    Precondition: v1 and v2 are 2D np.arrays
    '''
    return np.arccos(np.dot(v1, v2) / (np.linalg.norm(v1) * np.linalg.norm(v2)))

def orthogonal_converter(v1, v2):
    '''
    (np.array([float, float]), np.array([float, float])) -> float
    Returns the angle necessary to rotate v1 to be orthogonal to v2 in radians
    Precondition: v1 and v2 are 2D np.arrays
    '''
    return np.pi / 2 - angle_between(v1, v2)