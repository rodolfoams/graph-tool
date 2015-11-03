from random import shuffle, randint, random, choice
from ..core import Edge
from sys import maxint
from math import sqrt, ceil

mutationRate = 0.001
populationSize = 200
tournamentSize = 7
crossoverProbability = 0.85
eliteSize = 5

def totalCost(population):
    total = 0
    for p in population:
        total += p[1]
    return total

def cost(path, sparseMatrix):
    distance = 0
    for i in xrange(len(path)):
        source = path[i]
        target = path[(i+1)%len(path)]
        distance += sparseMatrix[source.index][target.index]
    return distance

def getFittest(population):
    bestPath = None
    bestDistance = maxint
    
    for individual in population:
        c = individual[1]
        if c < bestDistance:
            bestPath = individual[0]
            bestDistance = c
    return bestPath, bestDistance

def tournamentSelection(population):
    tournament = list()
    tCost = totalCost(population)
    weighedPopulation = [k for k in population for i in xrange(int(ceil(float(tCost)/k[1])))]
    for i in xrange(tournamentSize):
        tournament.append(choice(weighedPopulation))
    return getFittest(tournament)[0]

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

def evolvePopulation(population, sparseMatrix):
    population = sorted(population,key=lambda x: x[1])
    elite = population[:eliteSize]
    newPopulation = list()
    for i in xrange(eliteSize,populationSize):
        child = None
        if random() <= crossoverProbability:
            parent1 = tournamentSelection(population)
            parent2 = tournamentSelection(population)
            child = crossover(parent1,parent2)
        else:
            child = population[i][0]
        newPopulation.append(child)
    for i in xrange(populationSize-eliteSize):
        newPopulation[i] = mutate(newPopulation[i])
    return elite + [(x, cost(x,sparseMatrix)) for x in newPopulation]

def geneticSearch(graph, iterations=100):
    vertices = list(graph.vertices)
    population = list()
    sparseMatrix = graph.sparseMatrix
    bestPath = None
    bestDistance = maxint
    for i in xrange(populationSize):
        shuffle(vertices)
        aux = list(vertices)
        population.append((aux,cost(aux,sparseMatrix)))
    bestPath, bestDistance = getFittest(population) 
    for i in xrange(iterations):
        population = evolvePopulation(population,sparseMatrix)
        iterBestPath, iterBestDistance = getFittest(population) 
        if iterBestDistance < bestDistance:
            bestDistance = iterBestDistance
            bestPath = iterBestPath
        print bestDistance
    return bestDistance 
