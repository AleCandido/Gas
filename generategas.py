import random as rnd
from pylab import *

"""
Maybe I can factorize more in my generation functions. Indeed grid_generation and random_generation have a very similar backbone
"""

def grid_generation(particles, xpart, grid_len, density):
    """
    explores each position of a grid and randomly decides whether there is or not a particle there
    """
    for i in range(0,grid_len):
        for j in range(0,grid_len):
            s = 0       # kind of particle
            put = False                    
            while s<len(density) & put == False:
                if rnd.random()*100 < density[s]:
                    x = array([i-50, j-50])
                    v = array([rnd.random()*50 - 25, rnd.random()*50 - 25])
                    a = array([0, 0])
                    n = 1       # number of particles aggregated
                    newparticle = array([x, v, a, s, n])
                    
                    xpart[0] += [i]
                    xpart[1] += [j]
                    particles += [newparticle]
                    
                    put = True
                s += 1
                
            print(s, put)
                    
    return particles, xpart
        
def random_generation(particles, xpart, N_max, density):
    for n in range(0, N_max):
        s = 0
        put = False
        while s<len(density) & put == False:
            if rnd.random()*100 < density[s]:
                x = array([rnd.random()*100 -50, rnd.random()*100 -50])
                v = array([rnd.random()*50 - 25, rnd.random()*50 - 25])
                a = array([0, 0])
                n = 1       # number of particles aggregated
                newparticle = array([x, v, a, s, n])
        
                xpart[0] += x[0]
                xpart[1] += x[1]
                particles += [newparticle]
                
                s += 1
                put = True
                
    return particles, xpart