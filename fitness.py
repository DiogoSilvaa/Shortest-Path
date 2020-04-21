import random
import turtle
import math
import copy

def create_population(population, selected_map):
    gene_pool=[]
    for x in range(population):
        gene_pool.append(copy.deepcopy(selected_map))
        random.shuffle(gene_pool[x])
    return gene_pool

def fitness_function(gene_pool, best_solution):
    best_solution = copy.deepcopy(gene_pool[0])
    best_solution_score = 0
    ranking = []
    for x in range(len(gene_pool)):
        score = 0
        score += calculate_path(gene_pool[x])
        ranking.append(score)
        if score > best_solution_score:
            best_solution = x
            best_solution_score = score
    sorted_gene_pool = [x for _,x in sorted(zip(ranking,gene_pool), reverse=True)]
    print (sorted_gene_pool)
    return sorted_gene_pool, best_solution

def calculate_distance(starting_x, starting_y, destination_x, destination_y):
    distance = math.hypot(destination_x - starting_x, destination_y - starting_y)  
    return distance

def calculate_path(selected_map):
    distance = 0
    i = 0
    while i+1 < len(selected_map):
        distance = distance + calculate_distance(selected_map[i][0],selected_map[i][1],selected_map[i+1][0],selected_map[i+1][1])
        i=i+1
    distance = distance + calculate_distance(selected_map[i][0],selected_map[i][1],selected_map[0][0],selected_map[0][1])
    return distance

def generate_map(x_range, y_range, locations):
    generated_map=[]
    for x in range(locations):
        generated_map.append((random.randint(-(x_range),x_range),random.randint(-(y_range),y_range)))
    return generated_map
fitness_function(create_population(10,generate_map(50,50,10)),0)
