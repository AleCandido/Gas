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
    particles[i][0] = particles[i][0] + particles[i][2]
    particles[i][1] = particles[i][1] + particles[i][3]
    
    return particles

## expansion in a box
# a bit funnier
# is a 2D model, but it's immediately extensible to N dimensions

def box(particles, Lbox):
    for i in range(0,len(particles)):
        particles[i] = box1(particles[i], Lboox)
        
    return particles
    
def box1(particle, Lbox):
        futureposx = particle[0] + particle[2]
        futureposy = particle[1] + particle[3]
        if (futureposx > Lbox)|(futureposx < -Lbox):
            particle[2] = -particle[2]
            particle[0] = particle[0] + particle[2]
        else:
            particle[0] = futureposx
        if (futureposy > Lbox)|(futureposy < -Lbox):
            particle[3] = -particle[3]
            particle[1] = particle[1] + particle[3]
        else:
            particle[1] = futureposy
            
        return particle
    
## hard spheres collisions 2D
   
# distances
def edist(a,b):
    # euclidean distance
    return sqrt((a[0] - b[0])**2 + (a[1] - b[1])**2)
    
# evolutions
def hard_spheres(particles, radius, Lbox):
    for i in range(0, len(particles)): # implementare hard_spheres1, tipo box1, includendo tutto il for j
        for j in range(i + 1, len(particles)):
            x1 = array([particles[i][0], particles[i][1]])
            x2 = array([particles[j][0], particles[j][1]])
            dist = sqrt(sum((x1-x2)**2))     #this step can be implemented with another distance notion
            if (dist < 2*radius):
                p1 = array([particles[i][2], particles[i][3]])
                p2 = array([particles[j][2], particles[j][3]])
                par = array([x1[0] - x2[0], x1[1] - x2[1]])/dist
                ort = array([par[1], -par[0]])
                
                temp = sqrt(sum((p1*par)**2))*par + sqrt(sum((p2*ort)**2))*ort
                p2 = sqrt(sum((p2*par)**2))*par + sqrt(sum((p1*ort)**2))*ort
                p1 = temp
                
                particles[i][2] = p1[0]                
                particles[i][3] = p1[1]
                particles[j][2] = p2[0]                
                particles[j][3] = p2[1]
                
        particles[i] = box1(particles[i], Lbox)
        
    return particles