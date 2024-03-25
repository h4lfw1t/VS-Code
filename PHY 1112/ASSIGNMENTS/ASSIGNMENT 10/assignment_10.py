'''
Filename: assignment_10.py
Author: Patrick Geraghty
Date Created: 2024-03-25
Date Modified: 2024-03-25
Description: Assignment 9
'''

import numpy as np
import matplotlib.pyplot as plt

# Part 1

def decay_constant(half_life):          # function to calculate decay constant with half-life as input
    '''
    (float) -> float
    Returns the decay constant for a given half-life.
    Preconditions: half_life > 0
    '''
    # formula to calculate decay constant
    return np.log(2) / half_life

def dMdt(t, M):                         # function to calculate the derivative of M with respect to t. Note that in this case t is ambiguous.
    '''
    (float, float) -> float
    Returns the derivative of M with respect to t.
    Preconditions: M > 0
    '''
    # formula to calculate the derivative of M with respect to t
    return -decay_constant(0.52) * M

def dMdt_plot():                        # function to plot the derivative of M with respect to t
    '''
    () -> None
    Plots the derivative of M with respect to t.
    Preconditions: None
    '''
    plt.figure(1)                       # create a new figure
    M = np.linspace(0, 0.00000005)      # create an array of mass values from 0 to 5e-8
    y = dMdt(0, M)                      # calculate the derivative of M with respect to t for each mass value
    # plot the derivative of M with respect to t
    plt.plot(M, y, 'r', label='dM/dt = -λM(t)', linewidth=4, alpha=1)
    plt.xlabel('Mass (g)')              # set the x-axis label
    plt.ylabel('dM/dt')                 # set the y-axis label
    plt.title('dM/dt vs. Mass of Uranium-214')
    xtick_values = np.linspace(0, 5e-8, 6)
    x_tick_labels = [0, 10e-9, 20e-9, 30e-9, 40e-9, 50e-9]
    plt.xticks(xtick_values, x_tick_labels)
    plt.grid()
    plt.legend()
    plt.show()

def eulers_method(f, n, a, b, y0):
    h = (a - b) / n
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
    plt.axhline(tenth_step_euler[1][-1], color='r', linestyle='dashed', label=f'Initial Mass ({tenth_step_euler[1][-1]:.3e}g)')
    
    xtick_values = np.linspace(0, 2, 11)
    xtick_labels = [0, 0.2, 0.4, 0.6, 0.8, 1, 1.2, 1.4, 1.6, 1.8, 2]
    plt.xticks(xtick_values, xtick_labels)
    plt.xlabel('Time (ms)')
    plt.ylabel('Mass (g)')
    plt.title('Mass of Uranium-214 vs. Time')
    plt.grid()
    plt.legend()
    plt.show()

def hundredth_step_euler_plot():
    plt.figure(3)
    
    hundredth_step_euler = eulers_method(dMdt, -190, 1.9, 0, 2e-8)
    x, y = hundredth_step_euler
    
    plt.plot(x, y, 'b', label='Euler\'s Method with h = -0.01', linewidth=4, alpha=1)
    plt.axhline(hundredth_step_euler[1][-1], color='r', linestyle='dashed', label=f'Initial Mass ({hundredth_step_euler[1][-1]:.3e}g)')
    
    xtick_values = np.linspace(0, 2, 11)
    xtick_labels = [0, 0.2, 0.4, 0.6, 0.8, 1, 1.2, 1.4, 1.6, 1.8, 2]
    plt.xticks(xtick_values, xtick_labels)
    
    plt.xlabel('Time (ms)')
    plt.ylabel('Mass (g)')
    plt.title('Mass of Uranium-214 vs. Time')
    plt.grid()
    plt.legend()
    plt.show()

def analytical_solution(t, Ma, a):
    return Ma * np.e ** (-decay_constant(0.52) * (t - a))

def main():
    # Part 1
    print('Part 1')
    print(f'Decay constant for Uranium-214: {decay_constant(0.52)}/ms.')
    dMdt_plot()
    
    tenth_step_euler = eulers_method(dMdt, -19, 1.9, 0, 2e-8)
    hundredth_step_euler = eulers_method(dMdt, -190, 1.9, 0, 2e-8)
    
    print(f'Initial Mass of Uranium-214 using Euler\'s Method with h = -0.1: {tenth_step_euler[1][-1]}g.')
    print(f'Initial Mass of Uranium-214 using Euler\'s Method with h = -0.01: {hundredth_step_euler[1][-1]}g.')
    tenth_step_euler_plot()
    hundredth_step_euler_plot()
    
    print(f'Analytical solution for Uranium-214 at t = 0: {analytical_solution(0, 2e-8, 1.9)}g.')
    
    # Part 2

main()