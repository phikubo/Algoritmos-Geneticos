# Kling, Ronn. Learning DEAP from examples.

import matplotlib.pyplot as plt
import sys
import array
import random
import numpy as np
from deap import algorithms, base, creator, tools
import time
from covering_array import CA_k6_v5_t2, define_parameters
import pickle
import json
numCities = 20

'''
El objetivo de este script es guardar tres generaciones de soluciones, para procesarse después.

'''

# random.seed(0)
# x = np.random.rand(numCities)
# y = np.random.rand(numCities)
x = np.array([0.021336343039078498, 0.8557670487694291, 0.05899475456218195, 0.19876430792019661, 0.8546484948431854,
              0.1452711439416844, 0.9218814524796237, 0.6049816831567925, 0.7148588651154876, 0.7550115346544385,
              0.12600945687529663, 0.9804307024033798, 0.3546386362760232, 0.37995446055541915, 0.8513863669083543,
              0.8070644761904666, 0.04348802746101932, 0.9879168093086934, 0.9020196303856226, 0.1951517368443082])
y = np.array([0.7614910179984232, 0.6466075388766859, 0.5887040059688428, 0.16292913272219567, 0.6484738170998551,
              0.848979343250662, 0.5071465432722776, 0.07053194929165651, 0.3332973190746097, 0.198305673915544,
              0.6197464229820546, 0.6404080849321279, 0.9280039104875653, 0.2306101514238149, 0.7751164478818975,
              0.758512517427246, 0.31592417777156756, 0.6777592614748262, 0.5019632896829609, 0.9683180887820401])

# We want to minimize the distance so the weights have to be negative
creator.create("FitnessMin", base.Fitness, weights=(-1.0,))
#  The individuals are just single integer (typecode='i') array of dimension 1xnumCities
#  We also assign the creator.FitnessMin that was just created in the line above
creator.create("Individual", array.array, typecode='i', fitness=creator.FitnessMin)

def evalTSP(individual):
    diffx = np.diff(x[individual])
    diffy = np.diff(y[individual])
    distance = np.sum(diffx ** 2 + diffy ** 2)
    return distance,


def tsp_run(n=100, mate=tools.cxOrdered, cxpb=0.7, tournsize=5, mutpb=0.1, indpb=0.05):
    toolbox = base.Toolbox()
    # Attribute generator
    toolbox.register("indices", random.sample, range(numCities), numCities)
    toolbox.register("evaluate", evalTSP)
    # Structure initializers
    toolbox.register("individual", tools.initIterate, creator.Individual, toolbox.indices)
    toolbox.register("population", tools.initRepeat, list, toolbox.individual)
    if mate in [tools.cxUniform, tools.cxUniformPartialyMatched]:
        toolbox.register("mate", mate, indpb=0.015)
    else:
        toolbox.register("mate", mate)
    toolbox.register("mutate", tools.mutShuffleIndexes, indpb=indpb)
    toolbox.register("select", tools.selTournament, tournsize=tournsize)
    # start with a population of 300 individuals
    pop = toolbox.population(n=n)
    # only save the very best one
    hof = tools.HallOfFame(1)
    stats = tools.Statistics(lambda ind: ind.fitness.values)
    stats.register("avg", np.mean)
    stats.register("std", np.std)
    stats.register("min", np.min)
    stats.register("max", np.max)

    
    # use one of the built in GA's with a probablilty of mating of 0.7
    # a probability of mutating 0.2 and 140 generations.
    #ngen es el numero de generaciones
    numeroGeneracion=2
    poblacion,logbook=algorithms.eaSimple(pop, toolbox, cxpb=cxpb, mutpb=mutpb, ngen=numeroGeneracion, stats=stats, halloffame=hof)
    

 
    return pop, stats,hof, logbook, numeroGeneracion
    #stats.compile(pop), stats.compile(stats), stats.compile(hof)


def tuning_parameters():
    parameters_values = [[50, 75, 100, 125, 150],  # Population size
                         [tools.cxOrdered, tools.cxUniformPartialyMatched, tools.cxPartialyMatched, tools.cxOrdered,
                          tools.cxUniformPartialyMatched],  # Crossover operator
                         [0.6, 0.7, 0.8, 0.9, 1.0],  # Crossover probability
                         [5, 10, 15, 20, 25],  # Tournament size
                         [0.3, 0.25, 0.2, 0.15, 0.1],  # Mutation probability
                         [0.015, 0.03, 0.05, 0.08, 0.1]  # Gen mutation probability
                         ]
    f=[]
    sologen2=[]
    for i in range(len(CA_k6_v5_t2)):
        n, mate, cxpb, tournsize, mutpb, indpb = define_parameters(i, parameters_values, CA_k6_v5_t2)
        print ("n={}, mate={}, cxpb={}, tournsize={}, mutpb={}, indpb={}, run {}".format(n, mate, cxpb, tournsize, mutpb,
                                                                                        indpb, i))
        a,b,c,d, numgen = tsp_run(n=n, mate=mate, cxpb=cxpb, tournsize=tournsize, mutpb=mutpb, indpb=indpb)
        f.append(d)
    '''
    Por cada f hay: 38 configuraciones, y por cada configuracion hay tres generaciones o ngen generaciones
    '''
    for i in range(38):
        sologen2.append(f[i][numgen])
    print(len(f), type(f))
    print(">>>>>>>>>>>>>>>F: ",f[0][2]) #la ultima generacion en este caso 2, debe generalizar
    '''
    Ahora saco de la ultima generacion los valores que quiera plotear, esto debe hacerse desde el main
    '''
    return(sologen2)
    

        
    


def main():
    print ("Coordinate x", "\t", "Coordinate y")
    for xi, yi in zip(x, y):
        print (xi, "\t", yi)
    #plt.plot(x, y, 'o', color='black')
    pop, stats, hof, extrange = tsp_run()
    # plot the best one
    #-----print(type(stats))
    #print ("Solution: ", ind)
    #plt.figure(2)
    #plt.plot(x[ind], y[ind])
    #plt.show()


if __name__ == "__main__":
    #tuning_parameters()
    a=0
    dic=[]
    '''Ciclo para deterinar mas de un ciclo '''
    for i in range(2):
        
        print("---------------------------------------->it, ",a)
        dic.append(tuning_parameters())
        a+=1
    print(len(dic))
    with open("data_file.json", "w") as write_file:
        json.dump(dic, write_file)
    #main()
