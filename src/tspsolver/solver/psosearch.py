from math import fabs, floor
from random import random, randrange
from sys import maxint

particles = list()
particleCount = 10
numVertices = 0
vMax = 8.0
tolerance = 0.03
sparseMatrix = None
bestKnownDistance = 0.00000001

class Particle:
    def __init__(self):
        self.mData = [0] * numVertices
        self.mpBest = 0
        self.mVelocity = 0.0

    def getData(self, index):
        return self.mData[index]

    def setData(self, index, value):
        self.mData[index] = value

    def getPBest(self):
        return self.mpBest

    def setPBest(self, value):
        self.mpBest = value

    def getVelocity(self):
        return self.mVelocity

    def setVelocity(self, velocityScore):
        self.mVelocity = velocityScore

def getDistance(firstCity, secondCity):
    global sparseMatrix
    return sparseMatrix[firstCity][secondCity]

def getTotalDistance(index):
    particles[index].setPBest(0.0)
    
    for i in xrange(numVertices):
        particles[index].setPBest(particles[index].getPBest() + getDistance(particles[index].getData(i), particles[index].getData((i + 1)%numVertices)))
    
    return

def randomlyArrange(index = 0):
    cityA = randrange(0, numVertices)
    cityB = cityA
    
    while cityA == cityB:
        cityB = randrange(0, numVertices)
    
    temp = particles[index].getData(cityA)
    particles[index].setData(cityA, particles[index].getData(cityB))
    particles[index].setData(cityB, temp)
    return

def initializeParticles():
    global particles
    for i in xrange(particleCount):
        newParticle = Particle()
        
        for j in xrange(numVertices):
            newParticle.setData(j, j)
        
        particles.append(newParticle)
       
        for j in xrange(numVertices):
            randomlyArrange(i)
    
    for i in xrange(particleCount):
        getTotalDistance(i)
    particles = sorted(particles, key=lambda x: x.getPBest())

def updateVelocities():
    global vMax, particles
    worstResults = 0.0
    vValue = 0.0
    
    worstResults = particles[-1].getPBest()
    
    for i in xrange(particleCount):
        vValue = (vMax * particles[i].getPBest()) / worstResults
        
        if vValue > vMax:
            particles[i].setVelocity(vMax)
        elif vValue < 0.0:
            particles[i].setVelocity(0.0)
        else:
            particles[i].setVelocity(vValue)
    
    return

def copyFromParticle(source, destination):
    targetA = randrange(0, numVertices)
    targetB = 0
    indexA = 0
    indexB = 0
    tempIndex = 0
    
    for i in xrange(numVertices):
        if particles[source].getData(i) == targetA:
            targetB = particles[source].getData((i + 1)%numVertices)
            break
    
    for j in xrange(numVertices):
        if particles[destination].getData(j) == targetA:
            indexA = j
        
        if particles[destination].getData(j) == targetB:
            indexB = j
    
    tempIndex = (indexA + 1) % numVertices
    
    temp = particles[destination].getData(tempIndex)
    particles[destination].setData(tempIndex, particles[destination].getData(indexB))
    particles[destination].setData(indexB, temp)
    
    return


def updateParticles():
    for i in xrange(particleCount):
        if i > 0:
            changes = int(floor(fabs(particles[i].getVelocity())))
            for j in xrange(changes):
                if random() > 0.5:
                    randomlyArrange(i)
                copyFromParticle(i - 1, i)
            getTotalDistance(i)
    
    return
 
def PSOSearch(graph, bkd = 0.000001, epochs=10000):
    vertices = list(graph.vertices)
    global numVertices, particles, bestKnownDistance, sparseMatrix, particleCount
    particles = list()
    numVertices = len(vertices)
    particleCount = int(1.2*numVertices)
    bestKnownDistance = bkd
    sparseMatrix = list(graph.sparseMatrix)
    epoch = 0
    done = False
    initializeParticles()
    bestDistance = maxint
    while not done:
        bestDistance = int(min(particles[0].getPBest(),bestDistance))
        if epoch < epochs:
            for i in xrange(particleCount):
                if bestDistance <= (1+tolerance) * bestKnownDistance:
                    done = True
                    break

            updateVelocities()
            
            updateParticles()
            particles = sorted(particles, key=lambda x: x.getPBest()) 
            epoch += 1
        else:
            done = True
    return bestDistance
