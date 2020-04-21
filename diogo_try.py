import random
import math
import turtle
import copy
from functools import *

def generate_map_point(x_range, y_range, loc): #generates a random point
    #print("generating location point: " + str(loc))
    return (random.randint(-(x_range), x_range), random.randint(-(y_range), y_range))

def generate_map_points(x_range, y_range, locations): #generates a list of random points
    return list(map(partial(generate_map_point, x_range, y_range), range(locations)))

def generate_map_routes(map_points, total_routes): # generates different map routes
    map_routes=[]  
    for x in range(total_routes):
        print("map route: " + str(x))
        map_routes.append(copy.deepcopy(map_points))#populate in lecturer words
        random.shuffle(map_routes[x])
    return map_routes

def calculate_distance(starting_x, starting_y, destination_x, destination_y):
    distance = math.hypot(destination_x - starting_x, destination_y - starting_y)  
    return distance

def calculate_path(map_points):
    distance = 0
    i = 0
    while i+1 < len(map_points):
        distance = distance + calculate_distance(map_points[i][0],map_points[i][1],map_points[i+1][0],map_points[i+1][1])
        i=i+1
    distance = distance + calculate_distance(map_points[i][0],map_points[i][1],map_points[0][0],map_points[0][1])
    return distance

def fitness_function(map_routes,best_solution):
    best_solution = copy.deepcopy(map_routes[0])
    best_solution_score = 0
    ranking = []
    for x in range(len(map_routes)):
        score = 0
        score += calculate_path(map_routes[x])
        ranking.append(score)
        if score > best_solution_score:
            best_solution = x
            best_solution_score = score
    sorted_map_routes = [x for _,x in sorted(zip(ranking,map_routes), reverse=True)]
    return sorted_map_routes

def mating_function(map_routes, mutation_rate, elite_threshold):
    new_map_routes = []
    for x in map_routes:
        parent_1 = copy.deepcopy(map_routes[random.randint(0,int(len(map_routes)*elite_threshold))])
        parent_2 = copy.deepcopy(x)
        mutated_child = mutate(breed(parent_1,parent_2),mutation_rate)
        new_map_routes.append(mutated_child)
        print(new_map_routes)
    return new_map_routes

def breed(parent_1, parent_2):
    cut_points = []
    random_cut = random.uniform(0,1)
    rest_cut = 1-random_cut
    child = []
    dna_1 = []
    dna_2 = []
    x=0
    while x<=(len(parent_1)*random_cut):
        dna_1.append(random.choice(parent_1))
    while x<=(len(parent_2)*rest_cut):
        dna_2.append(random.choice(parent_2))
    child = dna_1 + dna_2
    return child

def mutate(child, mutation_rate):
    mutated_child=[]
    x=0
    for x in range(len(child)):
        if(random.random(0,1) < mutation_rate):
            y = random.randint (0,len(child)-1)
            dna_1 = child[x]
            dna_2 = child[y]
            child[x] = dna_2
            child[y] = dna_1
            mutated_child.append(child[y])
    return mutated_child


print("Welcome to salesman problem program \o/")
#print(mating_function((fitness_function(generate_map_routes((generate_map_points(50, 50, 10)),3),0),(generate_map_routes((generate_map_points(50, 50, 10)),3),0))0.5,0.1))

print(mating_function(fitness_function((generate_map_routes((generate_map_points(50, 50, 10)),3)),0),0.5,0.1))

#(generate_map_routes((generate_map_points(50, 50, 10)),3))
