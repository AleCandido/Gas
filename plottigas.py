from pylab import *
from mpl_toolkits.mplot3d import Axes3D

def plotparticles(particles,t):
    """
        Parameters
        ----------
        particles: 2D list of array, assuming zeroth and first element of the array as x-y positions
        
        Returns
        -------
        Show the picture of particles
    """
    xpart = zeros(len(particles))
    ypart = zeros(len(particles))
    
    for i in range(0,len(particles)):
        xpart[i] = particles[i][0][0]
        ypart[i] = particles[i][0][1]
    
    figure(t)
    xlim(min(xpart)*1.1,max(xpart)*1.1)
    ylim(min(ypart)*1.1,max(ypart)*1.1)
    plot(xpart, ypart, 'r.')
    

def plotparticles3D(particles,t):
    """
        Parameters
        ----------
        particles: 2D list of array, assuming zeroth and first element of the array as x-y positions
        
        Returns
        -------
        Show the picture of particles
    """
    xpart = zeros(len(particles))
    ypart = zeros(len(particles))
    zpart = zeros(len(particles))
    
    for i in range(0,len(particles)):
        xpart[i] = particles[i][0][0]
        ypart[i] = particles[i][0][1]
        zpart[i] = particles[i][0][2]
        
    fig = figure(t)
    ax = fig.add_subplot(111, projection='3d')
    
    ax.scatter(xpart, ypart, zpart, 'r.')

