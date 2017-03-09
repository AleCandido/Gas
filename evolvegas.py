from math import *
from pylab import array

"""
This library contains evolution functions of the gas system

Each function of this library has the base shape:
        Parameters
        ----------
        particles: 2D list of array
        other: external parameter describing the dynamics
        
        Returns
        -------
        particles: 2D list of array

    
Implemented:
    - free expansion
    - box constraint
"""

## free expansion
# the simpliest model
# is a 2D model, but it's immediately extensible to N dimensions

def free_expansion(particles):
    for i in range(0,len(particles)):
        particles[i][0] = particles[i][0] + particles[i][1]
    
    return particles

## expansion in a box
# a bit funnier
# is a 2D model, but it's immediately extensible to N dimensions

def box_constraint(particles, Lbox):
    for i in range(0,len(particles)):
        particles[i] = box1(particles[i], Lbox)
        
    return particles
    
def box1(particle, Lbox):
        futurepos = particle[0] + particle[1]
        for i in range(0, len(particle[0])):
            if (futurepos[i] > Lbox)|(futurepos[i] < -Lbox):
                particle[1][i] = -particle[1][i]
                particle[0][i] += particle[1][i]
            else:
                particle[0][i] = futurepos[i]
            
        return particle
    
## hard spheres collisions 2D
   
# distances
def edist(a,b):
    # euclidean distance
    return sqrt((a[0] - b[0])**2 + (a[1] - b[1])**2)
    
# evolutions
def hard_spheres(particles, Lbox, radius):
    # c'è da trasformarla in 3D
    # c'è da risolvere il problema della compenetrazione protratta su più step
    for i in range(0, len(particles)): # implementare hard_spheres1, tipo box1, includendo tutto il for j
        for j in range(i + 1, len(particles)):
            x1 = particles[i][0]
            x2 = particles[j][0]
            distance = sqrt(sum((x1-x2)**2))     # this step can be implemented with another distance notion
            if (distance == 0):
                distance = radius/10**6
                
            if (distance < 2*radius):
                # print(distance)
                v1 = particles[i][1]
                v2 = particles[j][1]
                par = (x1-x2)/distance              # the direction of the connection between centres
                ort = array([par[1], -par[0]])      # the direction orthogonal to par
                
                # if they hit each other they exchange the component of velocity in the direction of par
                # nothing happens in the ort direction
                temp = sqrt(sum((v2*par)**2))*par + sqrt(sum((v1*ort)**2))*ort
                v2 = sqrt(sum((v1*par)**2))*par + sqrt(sum((v2*ort)**2))*ort
                v1 = temp
                
                particles[i][1] = v1 
                particles[j][1] = v2
                
        particles[i] = box1(particles[i], Lbox)
        
    return particles

## long range interaction
# force
def Force(x):
    return 100/x**2

def direction(x1,x2):
    return array(x2 - x1)/sum((x1 - x2)**2)

# evolution
def long_interaction(particles, radius, Lbox):
    for i in range(0, len(particles)):
        [particles[i][4], particles[i][5]] = [0,0]
        
        for j in range(i + 1, len(particles)):
            x1 = array([particles[i][0], particles[i][1]])
            x2 = array([particles[j][0], particles[j][1]])
            distance = sqrt(sum((x1-x2)**2))

            F = Force(distance)
            [particles[i][4], particles[i][5]] = array([particles[i][4], particles[i][5]]) + direction(x1,x2)*F
            [particles[j][4], particles[j][5]] = array([particles[j][4], particles[j][5]]) + direction(x2,x1)*F
        
        particles[i] = box1(particles[i], Lbox)
        [particles[i][2], particles[i][3]] = array([particles[i][2], particles[i][3]]) + array([particles[i][4], particles[i][5]])
        
    return particles