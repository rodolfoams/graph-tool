#!/usr/bin/python

import sys
import time
from os import path
sys.path.append( path.dirname( path.dirname( path.abspath(__file__) ) ) )
from src import *

algorithms = [blindSearch,greedySearch,astarSearch]
strAlgorithms = ["blind","greedy","A*"]
datasets = ["brazil58","eil101","gil262"]
repetitions = 10

def main():
    outfile = open("results.csv","w")
    outfile.write('"algorithm","nodes","time","best"\n')
    for i in xrange(repetitions):
        for d in datasets:
            g = loadTSPLIBDataset(d)
            n = len(g.vertices)
            for j in xrange(len(algorithms)):
                a = algorithms[j]
                start = int(round(time.time()*1000))
                best = a(g)
                end = int(round(time.time()*1000))
                outfile.write(",".join([strAlgorithms[j],str(n),str(end-start),str(best)])+"\n")
                j += 1
    outfile.close()

if __name__ == "__main__":
    main()
