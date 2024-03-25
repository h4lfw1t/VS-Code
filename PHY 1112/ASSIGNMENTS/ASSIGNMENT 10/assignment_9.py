'''
Filename: assignment_9.py
Author: Patrick Geraghty
Date Created: 2024-03-25
Date Modified: 2024-03-25
Description: Assignment 9
'''

import numpy as np
import matplotlib.pyplot as plt

# Part 1

def decay_constant(half_life):
    '''
    (float) -> float
    Returns the decay constant for a given half-life.
    Preconditions: half_life > 0
    '''
    return np.log(2) / half_life

def dMdt(t, M):
    '''
    (float, float) -> float
    Returns the derivative of M with respect to t.
    Preconditions: M > 0
    '''
    return -decay_constant(0.52) * M

def dMdt_plot():
    plt.figure(1)
    M = np.linspace(0, 0.00000005)
    y = dMdt(0, M)
    plt.plot(M, y, 'r', label='dM/dt = -λM(t)', linewidth=4, alpha=1)
    plt.xlabel('Mass (m)')
    plt.ylabel('dM/dt')
    plt.title('dM/dt vs. Mass of Uranium-214')
    xtick_values = np.linspace(0, 5e-8, 6)
    x_tick_labels = [0, 10e-9, 20e-9, 30e-9, 40e-9, 50e-9]
    plt.xticks(xtick_values, x_tick_labels)
    plt.grid()
    plt.legend()
    plt.show()

def eulers_method(f, n, a, b, y0):
    h = (b - a) / n
    x = np.linspace(a, b, num=abs(n)+1)
    y = np.zeros(abs(n) + 1)
    y[0] = y0
    for i in range(abs(n)):
        y[i + 1] = y[i] + h * f(x[i], y[i])
    return x, y

def tenth_step_euler_plot():
    plt.figure(2)
    tenth_step_euler = eulers_method(dMdt, -19, 1.9, 0, 2e-8)
    x, y = tenth_step_euler
    plt.plot(x, y, 'b', label='Euler\'s Method with h = -0.1', linewidth=4, alpha=1)
    plt.xlabel('Time (s)')
    plt.ylabel('Mass (m)')
    plt.title('Mass of Uranium-214 vs. Time')
    plt.grid()
    plt.legend()
    plt.show()

def hundredth_step_euler_plot():
    plt.figure(3)
    hundredth_step_euler = eulers_method(dMdt, -190, 1.9, 0, 2e-8)
    x, y = hundredth_step_euler
    plt.plot(x, y, 'b', label='Euler\'s Method with h = -0.01', linewidth=4, alpha=1)
    plt.xlabel('Time (s)')
    plt.ylabel('Mass (m)')
    plt.title('Mass of Uranium-214 vs. Time')
    plt.grid()
    plt.legend()
    plt.show()

def main():
    # Part 1
    print('Part 1')
    print(f'Decay constant for Uranium-214: {decay_constant(0.52)}/ms.')
    dMdt_plot()
    
    tenth_step_euler = eulers_method(dMdt, -19, 1.9, 0, 2e-8)
    hundredth_step_euler = eulers_method(dMdt, -190, 1.9, 0, 2e-8)
    tenth_step_euler_plot()
    hundredth_step_euler_plot()