import sys
import random as rnd
from pylab import *
from plottigas import *
from evolvegas import *
from generategas import *

## set path
# to execute in future other manifactured modules (more fun!)
sys.path = sys.path + ["C:\\Users\\candi\\Documents\\Ale\\Python"]

## global variables

#initial values
grid_len = 100
N_max = 1000
density = array([0.1])
# density = sys.argv[0]
Lbox = 1000

#interaction values
sphere_radius = 20 # radius in hard-spheres model

## initial setting
particles = []

if sum(density) > 100:
    # normalizes probability of generating a particle to 1 if it exceeds
    density = density*100/sum(density)

particles = grid_generation(particles, grid_len, density)
    
## time evolution
t=0
# time 0 plot
plotparticles(particles, t)

# follow one particle evolution can be more interesting than look at the beginning and ending instant
onepx = [particles[0][0][0]]
onepy = [particles[0][0][1]]

# step by step evolution cycle
while t<100:
    particles = box_constraint(particles, Lbox)#sphere_radius, Lbox)
    onepx += [particles[0][0][0]]
    onepy += [particles[0][0][1]]
    t += 1

## end plots    
# one particle history  
figure(1)
plot(onepx,onepy)

# end positions
plotparticles(particles,t)