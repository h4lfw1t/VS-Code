'''
Filename:       a7_part2.py
Author:         Patrick Geraghty
Date Created:   2024-03-04
Date Modified:  2024-03-05
Description:    Assignment 7: Question 2. Racing to Shift Your Perspective
'''

import numpy as np
import matplotlib.pyplot as plt

# Question 2: Racing to Shift Your Perspective

import numpy as np
import matplotlib.pyplot as plt

def position(velocity, time):
    '''uses an outer product between velocity and time to generate 
    a 2d position array for all times where the columns are the vector 
    components and the rows represent different time points'''
    
    #### INSERT YOUR CODE HERE ####

    return np.outer(velocity, time)
    
    ###############################

def magnitude(vector):
    '''returns the square root of the inner product of vector with itself'''
   
    #### INSERT YOUR CODE HERE ####

    return np.sqrt(np.inner(vector, vector))
   
    ###############################

def determine_distances_and_winner(r1, s1, r2, s2):
    '''returns the final distances traveled by s1 (string) and s2 (string) 
    with position vectors r1 and r2, whose columns are the components 
    of the vector and whose rows represent different time points.
    It also returns a string regarding who won the race, s1 or s2
    if they tied, or if a winner cannot be determined'''

    #### INSERT YOUR CODE HERE ####

    final_distance_1 = str(magnitude(r1[:,-1]))     # final distance of s1
    final_distance_2 = str(magnitude(r2[:,-1]))     # final distance of s2
    # determine the winner given the final distances (conditional statements)
    if final_distance_1 < final_distance_2:
        string_with_winner = f'The {s2} wins!'
    elif final_distance_1 > final_distance_2:
        string_with_winner = f'The {s1} wins!'
    elif final_distance_1 == final_distance_2:
        string_with_winner = 'The vehicles tied!'
    else:
        string_with_winner = 'A winner cannot be determined'

    ###############################
        
    return final_distance_1, final_distance_2, string_with_winner


def road_reference_race():
    '''
    () -> None
    Plots the positions of the observer, car and truck over a 60 second race in increments of 5 seconds from the observer (road perspective). Prints positions over 5 second intervals, vehicles speeds, and distance from the origin after 60 seconds.
    Preconditions: None
    '''
    # the velocites are in the observer's frame of reference (road frame)
    v_observer= np.array([0,0])           # km/s
    v_car     = np.array([-15,125])/3600   # converted to km/s
    v_truck   = np.array([7,137])/3600    # converted to km/s

    t = np.linspace(0, 60, num=13)  # 0 to 60 seconds, in steps of 5 sec

    # calculate position vectors as a function of time
    r_observer = position(v_observer, t)
    r_car      = position(v_car, t)
    r_truck    = position(v_truck, t)

    # finding the final distances and the winner
    observer_dist = 0
    car_dist, truck_dist, winner_string = determine_distances_and_winner(r_car, "car", r_truck, "truck")

    # plot the positions of the observer, car and truck (rx versus ry for all the time points) with markers

    #### INSERT YOUR CODE HERE ####

    plt.figure(1)
    # plot the positions of the observer, car and truck
    plt.plot(r_observer[0], r_observer[1], 'ro', label=(f'Observer, travelled {float(observer_dist):.3f} km'))
    plt.plot(r_car[0], r_car[1], 'b+', label=(f'Car, travelled {float(car_dist):.3f} km'))
    plt.plot(r_truck[0], r_truck[1], 'gx', label=(f'Truck,  travelled {float(truck_dist):.3f} km'))

    ###############################

    plt.title(f"Trajectories during the race. {winner_string}")
    plt.xlabel("x axis (km)")
    plt.ylabel("y axis (km)")
    plt.axis("equal")
    plt.legend()
    plt.show()

    # print the positions of the observer, car and truck over 5 second intervals
    for i in range(0, len(t)):
        print(f"Time: {t[i]} seconds")
        print(f"Car position: x = {r_car[0,i]}, y = {r_car[1,i]}")
        print(f"Truck position: x = {r_truck[0,i]}, y = {r_truck[1,i]}")
        print()

    # print the speeds of the car and truck
    print(f'The car is travelling at {magnitude(v_car):.3f} km/s')
    print(f'The truck is travelling at {magnitude(v_truck):.3f} km/s', end='\n\n')

    # print the final distances of the car and truck
    print(f'The car is {float(car_dist):.3f} km from the origin after 60 seconds')
    print(f'The truck is {float(truck_dist):.3f} km from the origin after 60 seconds')

def transformed_race():
    '''
    () -> None
    Plots the positions of the observer, car and truck over a 60 second race in increments of 5 seconds from the car (car perspective). Prints positions over 5 second intervals, truck and car speeds, and distance from the origin after 60 seconds.'''
    # the velocites are in the observer's frame of reference (road frame)
    v_observer= np.array([0,0])           # km/s
    v_car     = np.array([-15,125])/3600   # converted to km/s
    v_truck   = np.array([7,137])/3600    # converted to km/s
    
    v_observer= v_observer - v_car
    v_truck   = v_truck - v_car
    v_car     = np.array([0,0]) # change this only after v_observer and v_truck


    t = np.linspace(0, 60, num=13)  # 0 to 60 seconds, in steps of 5 sec

    # calculate position vectors as a function of time
    r_observer = position(v_observer, t)
    r_car      = position(v_car, t)
    r_truck    = position(v_truck, t)

    # finding the final distances and the winner
    car_dist = 0
    observer_dist, truck_dist, winner_string = determine_distances_and_winner(r_observer, "observer", r_truck, "truck")

    # plot the positions of the observer, car and truck (rx versus ry for all the time points) with markers

    #### INSERT YOUR CODE HERE ####

    plt.figure(2)
    # plot the positions of the observer, car and truck
    plt.plot(r_observer[0], r_observer[1], 'ro', label=(f'Observer, travelled {float(observer_dist):.3f} km'))
    plt.plot(r_car[0], r_car[1], 'b+', label=(f'Car, travelled {float(car_dist):.3f} km'))
    plt.plot(r_truck[0], r_truck[1], 'gx', label=(f'Truck,  travelled {float(truck_dist):.3f} km'))

    ###############################

    plt.title(f"Trajectories during the race. {winner_string}")
    plt.xlabel("x axis (km)")
    plt.ylabel("y axis (km)")
    plt.axis("equal")
    plt.legend()
    plt.show()

    # print the positions of the observer and truck over 5 second intervals
    for i in range(0, len(t)):
        print(f"Time: {t[i]} seconds")
        print(f"Observer position: x = {r_observer[0,i]}, y = {r_observer[1,i]}")
        print(f"Truck position: x = {r_truck[0,i]}, y = {r_truck[1,i]}")
        print()

    # print the speeds of the observer and truck
    print(f'The observer is travelling at {magnitude(v_observer):.3f} km/s')
    print(f'The truck is travelling at {magnitude(v_truck):.3f} km/s', end='\n\n')

    # print the final distances of the observer and truck
    print(f'The observer is {float(observer_dist):.3f} km from the origin after 60 seconds')
    print(f'The truck is {float(truck_dist):.3f} km from the origin after 60 seconds')