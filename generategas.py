import random as rnd
from pylab import *

"""
Maybe I can factorize more in my generation functions. Indeed grid_generation and random_generation have a very similar backbone
"""

def grid_generation(particles, grid_len, density):
    """
    explores each position of a grid and randomly decides whether there is or not a particle there
    """
    for i in range(0,grid_len):
        for j in range(0,grid_len):
            s = 0       # kind of particle
            put = False                    
            while (s<len(density)) & (put == False):
                if rnd.random()*100 < density[s]:
                    x = array([i-50., j-50.])   # positions have to be floats
                    v = array([rnd.random()*50 - 25, rnd.random()*50 - 25])
                    a = array([0, 0])
                    n = 1       # number of particles aggregated
                    newparticle = array([x, v, a, s, n])
                    
                    particles += [newparticle]
                    
                    put = True
                s += 1
                    
    return particles
        
def random_generation(particles, N_max, density):
    for n in range(0, N_max):
        s = 0
        put = False
        while (s<len(density)) & (put == False):
            if (rnd.random()*100 < density[s]):
                x = array([rnd.random()*100 -50, rnd.random()*100 -50])
                v = array([rnd.random()*50 - 25, rnd.random()*50 - 25]) # posso implementare una distribuzione di maxwell sulle velocità
                a = array([0, 0])
                n = 1       # number of particles aggregated
                newparticle = array([x, v, a, s, n])
                
                particles += [newparticle]
                
                s += 1
                put = True
                
    return particles
    
def random_generation2(particles, grid_len, density, dimension):
    # se funziona sarà quella definitiva
    for s in range(0, len(density)):
        N_mean = grid_len**2*density[s]/100
        N = int(round(rnd.gauss(N_mean, N_mean/50)))
        for n in range(0, N):
            x = []
            v = []
            a = []
            for i in range(0, dimension):
                x += [rnd.random()*100 -50]
                v += [rnd.random()*50 - 25]
                a += [0.]
                
            x = array(x)
            v = array(v)
            a = array(a)
                
            n = 1       # number of particles aggregated
            newparticle = array([x, v, a, s, n])
            
            particles += [newparticle]
                
    return particles