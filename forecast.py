import random,array
from deap import creator, base, tools, algorithms
import fileinput
import glob
import re
import os
import pprint as pp

paths = ["./data/GOOG.csv"]

stockCloses = []
stockVolumes = []

for path in paths:
    for f in glob.glob(path):
        fo = open(f)
        lines = fo.readlines()
        counter = 0
        for line in lines:
            contents = line.split(",")
            if counter == 0:
                counter += 1
                continue
            stockCloses.append(float(contents[4]))
            stockVolumes.append(int(contents[5]))
            counter += 1
            pp.pprint(float(contents[4]))

        fo.close()


#create function for Fitness
def fitnessOfIndividual():
    #check with the current value in time -- hoping it converges

IND_SIZE = 10

#Fitness class
creator.create("FitnessMax", base.Fitness, weights = (1.0, ))

#Individual class
creator.create("Individual", list, fitness= creator.FitnessMin)

#Initialize the individual
toolbox = base.Toolbox()
toolbox.register("attr_float", random.random)
toolbox.register("individual", tools.initRepeat, creator.Individual, toolbox.attr_float, n=IND_SIZE)





