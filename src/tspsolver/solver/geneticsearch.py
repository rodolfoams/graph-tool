from random import shuffle, randint, random
from ..core import Edge
from sys import maxint
from math import sqrt, ceil

mutationRate = 0.015
populationSize = 50
tournamentSize = 5
eliteSize = 5

def strPath(path):
    vertices = map(str,[v.index for v in path])
    vertices.append(vertices[0])
    return "-".join(vertices)

def d(edge, edges):
    for e in edges:
        if e == edge:
            return e.weight

def cost(path, neighbors):
    distance = 0
    for i in xrange(len(path)):
        source = path[i]
        target = path[(i+1)%len(path)]
        edge = Edge(source, target,0,0)
        distance += d(edge, neighbors[source])
    return distance

def getFittest(population, neighbors):
    bestPath = None
    bestDistance = maxint
    
    for individual in population:
        c = cost(individual,neighbors)
        if c < bestDistance:
            bestPath = individual
            bestDistance = c
    return bestPath, bestDistance

def tournamentSelection(population, neighbors):
    tournament = list()
    for i in xrange(tournamentSize):
        randomId = randint(0,populationSize-1)
        tournament.append(population[randomId])
    return getFittest(tournament,neighbors)[0]

def crossover(p1, p2):
    child = [None] * len(p1)
    startPos = randint(0,len(p1))
    endPos = randint(0,len(p1))

    for i in xrange(len(p1)):
        if startPos < endPos and i > startPos and i < endPos:
            child[i] = p1[i]
        elif startPos > endPos:
            if not (i < startPos and i > endPos):
                    child[i] = p1[i]

    for i in xrange(len(p2)):
        if p2[i] not in child:
            for j in xrange(len(child)):
                if child[j] == None:
                    child[j] = p2[i]
                    break

    return child

def mutate(path):
    individual = list(path)
    for i in xrange(len(individual)):
        if random() < mutationRate:
            j = randint(0,len(individual)-1)
            aux = individual[j]
            individual[j] = individual[i]
            individual[i] = aux
    return individual

def evolvePopulation(population, neighbors):
    newPopulation = population[:eliteSize]
    for i in xrange(eliteSize,populationSize):
        parent1 = tournamentSelection(population, neighbors)
        parent2 = tournamentSelection(population,neighbors)
        child = crossover(parent1,parent2)
        newPopulation.append(child)
    for i in xrange(eliteSize,populationSize):
        newPopulation[i] = mutate(newPopulation[i])
    return newPopulation

def geneticSearch(graph, iterations=100):
    vertices = list(graph.vertices)
    population = list()
    neighbors = graph.neighbors
    bestPath = None
    bestDistance = maxint
    for i in xrange(populationSize):
        shuffle(vertices)
        aux = list(vertices)
        population.append(aux)
    bestPath, bestDistance = getFittest(population, neighbors)
    for i in xrange(iterations):
        population = sorted(population,key=lambda x: cost(x,neighbors))
        population = evolvePopulation(population, neighbors)
        iterBestPath, iterBestDistance = getFittest(population, neighbors)
        if iterBestDistance < bestDistance:
            bestDistance = iterBestDistance
            bestPath = iterBestPath
        print "Current best:", bestDistance
    return bestDistance 
