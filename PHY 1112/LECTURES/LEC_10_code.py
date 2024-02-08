import matplotlib.pyplot as plt
import numpy as np

def snells_law(n1,n2,theta_i):
    '''
    (float, float, float) -> float
    This function takes in the angle of incidence, and returns the angle of refraction.
    Preconditions: 0 <= theta_i <= pi/2, n1, n2 > 0
    '''
    
    return np.arcsin(n1/n2*np.sin(theta_i))

def refraction_plot_glass(n1,n2):
    '''
    (float, float) -> None
    This function takes in the angle of incidence, and plots the reflection coeffient as a function of the angle of incidence.
    Preconditions: 0 <= theta_i <= pi/2, n1, n2 > 0
    '''
    # Law of reflection: angle of incidence = angle of reflection
    # Snell's Law: n1*sin(theta1) = n2*sin(theta2)
    # Reflection Coefficient: r = (cos(theta1) - n2/n1*cos(theta2))/(cos(theta1) + n2/n1*cos(theta2))
    
    x = np.linspace(0, np.pi/2, 100)
    
    plt.figure(1)
    
    plt.plot(x, (n1*np.cos(x) - n2*np.cos(snells_law(n1,n2,x)))/(n1*np.cos(x) + n2*np.cos(snells_law(n1,n2,x))), label = 'Reflection Coefficient')
    
    plt.hlines(0, 0, np.pi/2, colors = 'k', linestyles = 'dashed')
    
    plt.xlim(0, np.pi/2)
    
    plt.xlabel('Angle of Incidence (radians)')
    plt.ylabel('Reflection Coefficient')
    plt.title('Reflection Coefficient as a Function of Angle of Incidence')
    plt.legend()
    
    plt.grid()
    
    plt.show()