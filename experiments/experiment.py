#!/usr/bin/python

import sys
import time
from os import path
sys.path.append( path.dirname( path.dirname( path.abspath(__file__) ) ) )
from src import *
from random import shuffle

algorithms = [blindSearch,greedySearch,geneticSearch]
#algorithms = [blindSearch,greedySearch]
#algorithms = [astarSearch]
strAlgorithms = ["blind","greedy","genetic"]
#strAlgorithms = ["blind","greedy"]
#strAlgorithms = ["A*"]
datasets = ["brazil58","eil101","gil262"]
repetitions = 5 
#repetitions = 1

def main():
    graphs = list()
    results = list()
    print '"algorithm","numCities","processingTime","bestDistanceFound","tspInstance"'
    for d in datasets:
        graphs.append(loadTSPLIBDataset(d))
    for i in xrange(repetitions):
        d = 0
        for g in graphs:
            n = len(g.vertices)
            for j in xrange(len(algorithms)):
                a = algorithms[j]
                start = int(round(time.time()*1000))
                bestFound = a(g)
                end = int(round(time.time()*1000))
                print ",".join([strAlgorithms[j],str(n),str(end-start),str(bestFound),datasets[d]])
            d += 1

if __name__ == "__main__":
    main()
