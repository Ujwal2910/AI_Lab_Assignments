import random
import math
import getopt
import sys
import GeneticAlgorithm

#generating random cities --
# Number of cities
citiesN = 10
# x & y range for positions
width = 10
height = 10

# -- Config for Generic Algorithm
# The number of routes in each generation.
population = 3
#Number of generations.
generations = 150
#change a crossover 
#old generation to the next.
crossoverChance = 0.7
#change of a mutation for each route
#generation to the next.
mutationChance = 0.5


class Route(GeneticAlgorithm.SolutionCandidate):
        def __init__(self, cities):
                self.cities = cities
                
        def _distance(self, city1, city2):
                """Calculate the distance between two cities."""
                return math.hypot(city2[0] - city1[0],
                                  city2[1] - city1[1])
	
        def getLength(self):
                """Calculate the length of the route."""
                return sum([self._distance(self.cities[i-1],
                                           self.cities[i]) \
                                    for i in range(len(self.cities))])
        
        def getFitness(self):
                return 1 / pow(self.getLength(), 2)

        def crossover(self, route):
                """Take a cross-section of this instance and swap it
                with a cross-section of route."""
                x1 = len(self.cities) / 3
                x2 = x1 * 2
                routes = [self.cities, route.cities]
                
                crossParts = [r[x1:x2] for r in routes]	
                crossParts.reverse()
	
                for i in range(len(routes)):   
                        route = routes[i]
                        cross = crossParts[i]

                        for j in range(x1) + range(x2, len(route)):
                                while route[j] in cross:
                                        route[j] = crossParts[i-1][cross.index(route[j])]
                        for j in range(x1,x2):
                                route[j] = cross[j-x1]
                                
        def mutate(self):
                """Swap two cities."""
                index1 = random.randint(0, len(self.cities) - 1)
                index2 = random.randint(0, len(self.cities) - 1)
                n = self.cities[index1]
                self.cities[index1] = self.cities[index2]
                self.cities[index2] = n

        def copy(self):
                return Route(self.cities[:])
                
class RandomRouteFactory(GeneticAlgorithm.SolutionCandidateFactory):
        def __init__(self, cities):
                self.cities = cities
                
        def generate(self):
                cities = self.cities[:]
                random.shuffle(cities)
                return Route(cities)

def usage ():
        print "Usage tsp.py [-h -r -i image.svg]"

def generateRandomCities(n, width, height):
        return [[random.randint(0,width),
                 random.randint(0,height)] for x in range(n)]

def parseCities(args):
        cities = []
        for arg in args:
                arg = arg.split(',')
                if len(arg) == 2:
                        cities.append([int(arg[0]), int(arg[1])])        
        return cities

def writeMap(mapFile, route):
        f = open(mapFile, 'w')
        f.write(route.createMap())
        f.close()

cityPositions = []
mapFile = False

opts, args = getopt.getopt(sys.argv[1:], "hri:")

for opt, value in opts:
        if opt == '-h':
                usage()
                exit()
        elif opt == '-r':
                cityPositions = generateRandomCities(citiesN, width, height)
        elif opt == '-i':
                mapFile = value

if cityPositions == []:
        cityPositions = parseCities(args)

if cityPositions == []:
        usage()
        exit(1)
        
generator = RandomRouteFactory(cityPositions)
ga = GeneticAlgorithm.GeneticAlgorithm(generator,
                                       crossoverChance,
                                       mutationChance,
                                       population)
print "Generation\tAvg\tShortest"
for i in range(generations):
        # create a new generation
	ga.evolve()

        # Calculate the lengths of the routes
	lengths = [route.getLength() for route in ga.getSolutions()]
        
        # Print the avg length and the length of the shortest route
	print i + 1,"\t", \
            int(sum(lengths) / len(lengths)),"\t", \
            int(min(lengths))

shortest = ga.getBestSolution()

print "Shortest route: " + "--> ".join([str(pos[0]) + "," + str(pos[1]) \
                                             for pos in shortest.cities])

if mapFile != False:
        writeMap(mapFile, shortest)
