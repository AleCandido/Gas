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
density = array([1.])
# density = sys.argv[0]
Lbox = 200

#interaction values
sphere_radius = 1 # radius in hard-spheres model

## initial setting
particles = []

if sum(density) > 100:
    # normalizes probability of generating a particle to 1 if it exceeds
    density = density*100/sum(density)

particles = random_generation2(particles, grid_len, density, 3)
    
## time evolution
t=0
# time 0 plot
plotparticles3D(particles, t)

# follow one particle evolution can be more interesting than look at the beginning and ending instant
onep = []

for i in range(0,len(particles[0][0])):
    onep += [0]
    onep[i] = [particles[0][0][i]]

# step by step evolution cycle
while t<100:
    particles = box_constraint(particles, Lbox)
    for i in range(0,len(particles[0][0])):
        onep[i] += [particles[0][0][i]]
    t += 1

## end plots    
# one particle history  
fig = figure(1)
ax = fig.gca(projection='3d')
ax.plot(onep[0], onep[1], onep[2], label='0th particle trajectory')
ax.legend()

# plot(onep[0],onep[1])

# end positions
plotparticles3D(particles,t)