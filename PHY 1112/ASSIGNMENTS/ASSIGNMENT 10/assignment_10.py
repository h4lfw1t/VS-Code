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

def decay_constant(half_life):                                                  # function to calculate decay constant with half-life as input
    '''
    (float) -> float
    Returns the decay constant for a given half-life.
    Preconditions: half_life > 0
    '''
    # formula to calculate decay constant
    return np.log(2) / half_life

def dMdt(t, M):                                                                 # function to calculate the derivative of M with respect to t. Note that in this case t is ambiguous.
    '''
    (float, float) -> float
    Returns the derivative of M with respect to t.
    Preconditions: M > 0
    '''
    # formula to calculate the derivative of M with respect to t
    return -decay_constant(0.52) * M

def dMdt_plot():                                                                # function to plot the derivative of M with respect to t
    '''
    () -> None
    Plots the derivative of M with respect to t.
    Preconditions: None
    '''
    plt.figure(1)                                                               # create a new figure
    M = np.linspace(0, 0.00000005)                                              # create an array of mass values from 0 to 5e-8
    y = dMdt(0, M)                                                              # calculate the derivative of M with respect to t for each mass value
    
    plt.plot(M, y, 'r', label='dM/dt = -λM(t)', linewidth=4, alpha=1)           # plot the derivative of M with respect to t
    plt.xlabel('Mass (g)')                                                      # set the x-axis label
    plt.ylabel('dM/dt')                                                         # set the y-axis label
    plt.title('dM/dt vs. Mass of Uranium-214')                                  # set the title of the plot
    xtick_values = np.linspace(0, 5e-8, 6)                                      # set the x-tick values
    x_tick_labels = [0, 10e-9, 20e-9, 30e-9, 40e-9, 50e-9]                      # set the x-tick labels
    plt.xticks(xtick_values, x_tick_labels)                                     # set the x-ticks
    plt.grid()                                                                  # add a grid to the plot
    plt.legend()                                                                # add a legend to the plot
    plt.show()

def eulers_method(f, n, a, b, y0):                                              # general function for Euler's Method
    h = (a - b) / n                                                             # calculate the step size, reversed a and b to account for negative n
    x = np.linspace(a, b, num=abs(n)+1)                                         # create an array of time values from a to b, using abs(n) to account for negative n
    y = np.zeros(abs(n) + 1)                                                    # create an array of zeros with length abs(n) + 1
    y[0] = y0                                                                   # set the initial value
    for i in range(abs(n)):                                                     # iterate through the time values
        y[i + 1] = y[i] + h * f(x[i], y[i])                                     # calculate the next value of y
    return x, y                                                                 # return the x values and y values

def tenth_step_euler_plot():                                                    # function to plot the mass of Uranium-214 using Euler's Method with h = -0.1
    plt.figure(2)                                                               # create a new figure
    
    tenth_step_euler = eulers_method(dMdt, -19, 1.9, 0, 2e-8)                   # calculate the mass of Uranium-214 using Euler's Method with h = -0.1
    x, y = tenth_step_euler                                                     # unpack the x values and y values
    
    # plot the mass of Uranium-214 using Euler's Method with h = -0.1, followed by a dashed line representing the initial mass
    plt.plot(x, y, 'b', label='Euler\'s Method with h = -0.1', linewidth=4, alpha=1)
    plt.axhline(tenth_step_euler[1][-1], color='r', linestyle='dashed', label=f'Initial Mass ({tenth_step_euler[1][-1]:.3e}g)')
    
    xtick_values = np.linspace(0, 2, 11)                                        # set the x-tick values
    xtick_labels = [0, 0.2, 0.4, 0.6, 0.8, 1, 1.2, 1.4, 1.6, 1.8, 2]            # set the x-tick labels
    plt.xticks(xtick_values, xtick_labels)                                      # set the x-ticks
    
    plt.xlabel('Time (ms)')                                                     # set the x-axis label
    plt.ylabel('Mass (g)')                                                      # set the y-axis label
    plt.title('Mass of Uranium-214 vs. Time')                                   # set the title of the plot
    plt.grid()                                                                  # add a grid to the plot
    plt.legend()                                                                # add a legend to the plot
    plt.show()

def hundredth_step_euler_plot():                                                # function to plot the mass of Uranium-214 using Euler's Method with h = -0.01
    plt.figure(3)                                                               # create a new figure
    
    hundredth_step_euler = eulers_method(dMdt, -190, 1.9, 0, 2e-8)              # calculate the mass of Uranium-214 using Euler's Method with h = -0.01
    x, y = hundredth_step_euler                                                 # unpack the x values and y values
    
    # plot the mass of Uranium-214 using Euler's Method with h = -0.01, followed by a dashed line representing the initial mass
    plt.plot(x, y, 'b', label='Euler\'s Method with h = -0.01', linewidth=4, alpha=1)
    plt.axhline(hundredth_step_euler[1][-1], color='r', linestyle='dashed', label=f'Initial Mass ({hundredth_step_euler[1][-1]:.3e}g)')
    
    xtick_values = np.linspace(0, 2, 11)                                        # set the x-tick values
    xtick_labels = [0, 0.2, 0.4, 0.6, 0.8, 1, 1.2, 1.4, 1.6, 1.8, 2]            # set the x-tick labels
    plt.xticks(xtick_values, xtick_labels)                                      # set the x-ticks
    
    plt.xlabel('Time (ms)')                                                     # set the x-axis label
    plt.ylabel('Mass (g)')                                                      # set the y-axis label
    plt.title('Mass of Uranium-214 vs. Time')                                   # set the title of the plot
    plt.grid()                                                                  # add a grid to the plot
    plt.legend()                                                                # add a legend to the plot
    plt.show()

def analytical_solution(t, Ma, a):                                              # function to calculate the analytical solution for the mass of Uranium-214
    return Ma * np.e ** (-decay_constant(0.52) * (t - a))                       

# Part 2

def euler_solver_2o(f, g, a, b, ua, va, n, gamma=0.15):                         # function to solve a system of 2 ODEs using Euler's Method
    '''
    (function, function, float, float, float, float, int) -> np.array, np.array, np.array
    Returns the x values, u(x) values, and v(x) values for a second order ODE using Euler's Method.
    Preconditions: f and g must be ODEs of the form f(x, u, v) and g(x, u, v)
    '''
    h = (b - a) / n                                                             # calculate the step size
    x = np.linspace(a, b, n + 1)                                                # create an array of x values from a to b
    u = np.zeros(n + 1)                                                         # create an array of zeros with length n + 1
    v = np.zeros(n + 1)                                                         # create an array of zeros with length n + 1
    u[0] = ua                                                                   # set the initial value of u
    v[0] = va                                                                   # set the initial value of v
    for i in range(n):                                                          # iterate through the x values
        u[i + 1] = u[i] + h * f(x[i], u[i], v[i])                               # calculate the next value of u
        v[i + 1] = v[i] + h * g(x[i], u[i], v[i], gamma)                        # calculate the next value of v
    return x, u, v                                                              # return the x values, u values, and v values

def f(x, u, v):                                                                 # function to calculate the derivative of u with respect to x
    '''
    (float, float, float) -> float
    Returns the derivative of u with respect to x.
    Preconditions: None
    '''
    return v

def g(x, u, v, gamma):                                                          # function to calculate the derivative of v with respect to x
    '''
    (float, float, float) -> float
    Returns the derivative of v with respect to x.
    Preconditions: None
    '''
    return -gamma * v - u

def damped_harmonic_motion_plot():                                              # function to plot the solution to the second order ODE
    plt.figure(4)                                                               # create a new figure
    
    euler_2o = euler_solver_2o(f, g, 0, 20 * np.pi, 1, 0, 20000)                # calculate the solution to the second order ODE
    x, u, v = euler_2o                                                          # unpack the x values, u values, and v values
    
    # plot the solution to the second order ODE
    plt.plot(x, u, 'b', label='u(x)', linewidth=4, alpha=1)
    plt.plot(x, v, 'r', label='v(x)', linewidth=4, alpha=1)
    plt.plot(x, np.sqrt(u ** 2 + v ** 2), 'g', label='u(x) + v(x)', linewidth=4, alpha=1)
    
    xtick_values = np.linspace(0, 20 * np.pi, 11)                               # set the x-tick values
    xtick_labels = [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20]                      # set the x-tick labels
    plt.xticks(xtick_values, xtick_labels)                                      # set the x-ticks
    
    plt.xlabel('Time (t)')                                                      # set the x-axis label
    plt.ylabel('Displacement (m)')                                              # set the y-axis label
    plt.title('Damped Harmonic Motion of a Spring')                             # set the title of the plot
    plt.grid()                                                                  # add a grid to the plot
    plt.legend()                                                                # add a legend to the plot
    plt.show()

def damped_harmonic_motion_plot_increase_h():                                   # function to plot the solution to the second order ODE
    plt.figure(5)                                                               # create a new figure
    
    euler_2o = euler_solver_2o(f, g, 0, 20 * np.pi, 1, 0, 200000)               # calculate the solution to the second order ODE with increased h
    x, u, v = euler_2o                                                          # unpack the x values, u values, and v values
    
    # plot the solution to the second order ODE
    plt.plot(x, u, 'b', label='u(x)', linewidth=4, alpha=1)
    plt.plot(x, v, 'r', label='v(x)', linewidth=4, alpha=1)
    plt.plot(x, np.sqrt(u ** 2 + v ** 2), 'g', label='u(x) + v(x)', linewidth=4, alpha=1)
    
    xtick_values = np.linspace(0, 20 * np.pi, 11)                               # set the x-tick values
    xtick_labels = [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20]                      # set the x-tick labels
    plt.xticks(xtick_values, xtick_labels)                                      # set the x-ticks
    
    plt.xlabel('Time (t)')                                                      # set the x-axis label
    plt.ylabel('Displacement (m)')                                              # set the y-axis label
    plt.title('Damped Harmonic Motion of a Spring with larger h')               # set the title of the plot
    plt.grid()                                                                  # add a grid to the plot
    plt.legend()                                                                # add a legend to the plot
    plt.show()

def damped_harmonic_motion_plot_decrease_h():                                   # function to plot the solution to the second order ODE
    plt.figure(6)                                                               # create a new figure
    
    euler_2o = euler_solver_2o(f, g, 0, 20 * np.pi, 1, 0, 2000)                 # calculate the solution to the second order ODE with decreased h
    x, u, v = euler_2o                                                          # unpack the x values, u values, and v values
    
    # plot the solution to the second order ODE
    plt.plot(x, u, 'b', label='u(x)', linewidth=4, alpha=1)
    plt.plot(x, v, 'r', label='v(x)', linewidth=4, alpha=1)
    plt.plot(x, np.sqrt(u ** 2 + v ** 2), 'g', label='u(x) + v(x)', linewidth=4, alpha=1)
    
    xtick_values = np.linspace(0, 20 * np.pi, 11)                               # set the x-tick values
    xtick_labels = [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20]                      # set the x-tick labels
    plt.xticks(xtick_values, xtick_labels)                                      # set the x-ticks
    
    plt.xlabel('Time (t)')                                                      # set the x-axis label
    plt.ylabel('Displacement (m)')                                              # set the y-axis label
    plt.title('Damped Harmonic Motion of a Spring with smaller h')              # set the title of the plot
    plt.grid()                                                                  # add a grid to the plot
    plt.legend()                                                                # add a legend to the plot
    plt.show()

def damped_harmonic_motion_plot_increase_gamma():                               # function to plot the solution to the second order ODE
    plt.figure(7)                                                               # create a new figure
    
    euler_2o = euler_solver_2o(f, g, 0, 20 * np.pi, 1, 0, 20000, 1.5)           # calculate the solution to the second order ODE with increased gamma
    x, u, v = euler_2o                                                          # unpack the x values, u values, and v values
    
    # plot the solution to the second order ODE
    plt.plot(x, u, 'b', label='u(x)', linewidth=4, alpha=1)
    plt.plot(x, v, 'r', label='v(x)', linewidth=4, alpha=1)
    plt.plot(x, np.sqrt(u ** 2 + v ** 2), 'g', label='u(x) + v(x)', linewidth=4, alpha=1)
    
    xtick_values = np.linspace(0, 20 * np.pi, 11)                               # set the x-tick values
    xtick_labels = [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20]                      # set the x-tick labels
    plt.xticks(xtick_values, xtick_labels)                                      # set the x-ticks
    
    plt.xlabel('Time (t)')                                                      # set the x-axis label
    plt.ylabel('Displacement (m)')                                              # set the y-axis label
    plt.title('Damped Harmonic Motion of a Spring with increased gamma')                             # set the title of the plot
    plt.grid()                                                                  # add a grid to the plot
    plt.legend()                                                                # add a legend to the plot
    plt.show()

def damped_harmonic_motion_plot_decrease_gamma():                               # function to plot the solution to the second order ODE
    plt.figure(8)                                                               # create a new figure
    
    euler_2o = euler_solver_2o(f, g, 0, 20 * np.pi, 1, 0, 20000, 0.015)         # calculate the solution to the second order ODE with decreased gamma
    x, u, v = euler_2o                                                          # unpack the x values, u values, and v values
    
    # plot the solution to the second order ODE
    plt.plot(x, u, 'b', label='u(x)', linewidth=4, alpha=1)
    plt.plot(x, v, 'r', label='v(x)', linewidth=4, alpha=1)
    plt.plot(x, np.sqrt(u ** 2 + v ** 2), 'g', label='u(x) + v(x)', linewidth=4, alpha=1)
    
    xtick_values = np.linspace(0, 20 * np.pi, 11)                               # set the x-tick values
    xtick_labels = [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20]                      # set the x-tick labels
    plt.xticks(xtick_values, xtick_labels)                                      # set the x-ticks
    
    plt.xlabel('Time (t)')                                                      # set the x-axis label
    plt.ylabel('Displacement (m)')                                              # set the y-axis label
    plt.title('Damped Harmonic Motion of a Spring with decreased gamma')        # set the title of the plot
    plt.grid()                                                                  # add a grid to the plot
    plt.legend()                                                                # add a legend to the plot
    plt.show()

def damped_harmonic_motion_plot_zero_gamma():                                   # function to plot the solution to the second order ODE
    plt.figure(9)                                                               # create a new figure
    
    euler_2o = euler_solver_2o(f, g, 0, 20 * np.pi, 1, 0, 20000, 0)             # calculate the solution to the second order ODE with gamma = 0
    x, u, v = euler_2o                                                          # unpack the x values, u values, and v values
    
    # plot the solution to the second order ODE
    plt.plot(x, u, 'b', label='u(x)', linewidth=4, alpha=1)
    plt.plot(x, v, 'r', label='v(x)', linewidth=4, alpha=1)
    plt.plot(x, np.sqrt(u ** 2 + v ** 2), 'g', label='u(x) + v(x)', linewidth=4, alpha=1)
    
    xtick_values = np.linspace(0, 20 * np.pi, 11)                               # set the x-tick values
    xtick_labels = [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20]                      # set the x-tick labels
    plt.xticks(xtick_values, xtick_labels)                                      # set the x-ticks
    
    plt.xlabel('Time (t)')                                                      # set the x-axis label
    plt.ylabel('Displacement (m)')                                              # set the y-axis label
    plt.title('Damped Harmonic Motion of a Spring, gamma = 0')                  # set the title of the plot
    plt.grid()                                                                  # add a grid to the plot
    plt.legend()                                                                # add a legend to the plot
    plt.show()

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
    print()
    print()
    print()
    
    # Part 2
    print('Part 2')
    euler_2o_v1 = euler_solver_2o(f, g, 0, 20 * np.pi, 1, 0, 20000)
    print('x: ',euler_2o_v1[0])
    print('u: ',euler_2o_v1[1])
    print('v: ',euler_2o_v1[2])
    
    damped_harmonic_motion_plot()
    damped_harmonic_motion_plot_increase_h()
    damped_harmonic_motion_plot_decrease_h()
    damped_harmonic_motion_plot_increase_gamma()
    damped_harmonic_motion_plot_decrease_gamma()
    damped_harmonic_motion_plot_zero_gamma()

main()