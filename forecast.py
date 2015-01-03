import random,array
from deap import creator, base, tools, algorithms
import fileinput
import glob
import re
import os
import pprint as pp

paths = ["../data/GOOG.csv"]

stockValues = []

for path in paths:
    for f in glob.glob(path):
        fo = open(f)
        lines = fo.readlines()
        for line in lines:
            contents = line.split(",")


