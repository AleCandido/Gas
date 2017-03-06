import sys
import random as rnd
from pylab import *
from plottigas import *
from evolvegas import *

## set path
# to execute in future other manifactured modules (more fun!)
sys.path = sys.path + ["C:\\Users\\candi\\Documents\\Ale\\Python"]


## global variables

#initial values
grid_len = 100
density = 3
# density = sys.argv[0]
Lbox = 1000

#interaction values
sphere_radius = 20 # radius in hard-spheres model

## initial setting
particles = []
xpart = []
ypart = []

# explores each position of a grid and randomly decides whether there is or not a particle there
for i in range(0,grid_len):
    for j in range(0,grid_len):
        if rnd.random()*100 < density:
            newparticle = array([i-50, j-50, rnd.random()*50 - 25, rnd.random()*50 - 25 ])
            xpart += [i]
            ypart += [j]
            particles += [newparticle]
        #elif rnd.random()*100 < (density1 + density2):
            
    
## time evolution
t=0
# time 0 plot
plotparticles(particles, t)

# follow one particle evolution can be more interesting than look at the beginning and ending instant
onepx = [particles[0][0]]
onepy = [particles[0][1]]

# step by step evolution cycle
while t<100:
    particles = hard_spheres(particles, sphere_radius, Lbox)
    onepx += [particles[0][0]]
    onepy += [particles[0][1]]
    t += 1

## end plots    
# one particle history  
figure(1)
plot(onepx,onepy)

# end positions
plotparticles(particles,t)