import random
import turtle
import math
import copy

def student_details():
    # add variables to store student ID and username to be returned
    student_id = 17071828
    student_username = 'dd18aaz'
    return student_id, student_username

def generate_map(x_range, y_range, locations):
    generated_map=[]
    for x in range(locations):
        generated_map.append((random.randint(-(x_range),x_range),random.randint(-(y_range),y_range)))
    return generated_map

def print_map(speed, color, thickness, selected_map):
    print("printing map")
    i=1
    turtle.penup()
    turtlegoto(selected_map[0])
    while i+1 < len(selected_map):
        turtle.pendown()
        turtle.goto(selected_map[i])
        turtle.goto(selected_map[i+1])
        i+=1
        turtle.penup()
    return 0
    
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

#################################################################################################

def nearest_neighbour_algorithm(selected_map):
    temp_map = copy.deepcopy(selected_map)
    optermised_map = []
    optermised_map.append(temp_map.pop())
    for x in range(len(temp_map)):
        nearest_value = 100000
        nearest_index = 0
        for i in range(len(temp_map)):
            current_value = calculate_distance(selected_map[x][0],selected_map[x][1],selected_map[i][0],selected_map[i][1]) 
            if nearest_value > current_value:
                nearest_value = current_value
                nearest_index = i
        optermised_map.append(temp_map[nearest_index])
        del temp_map[nearest_index]
    return optermised_map

#################################################################################################

def genetic_algorithm(selected_map, population, iterations, mutation_rate, elite_threshold):
    return best_solution

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

def iterator(gene_pool, iterations, mutation_rate, elite_threshold):
    return best_solution

def mating_function(gene_pool, best_solution, mutation_rate, elite_threshold):
    new_gene_pool = []
    for x in gene_pool:
        parent_1 = copy.deepcopy(gene_pool[random.randint(0,int(len(gene_pool)*elite_threshold))])
        parent_2 = copy.deepcopy(x)
        mutated_child = mutate(breed(parent_1,parent_2),mutation_rate)
        new_gene_pool.append(mutated_child)
    return new_gene_pool

def breed(parent_1, parent_2):
    cut_points = []
    random_cut = random.randint(0,len(parent_1))
    rest_cut = 1-random_cut
    child = []
    dna_1 = []
    dna_2 = []
    while x<=(len(parent_1)*random_cut):
        dna_1.append(random.choice(parent_1))
    while x<=(len(parent_2)*rest_cut):
        dna_2.append(random.choice(parent_2))
    child = dna_1 + dna_2
    return child

def mutate(child, mutation_rate):
    mutated_child=[]
    for x in range(len(child)):
        if(random.random(0,1) < mutation_rate):
            y = random.randint (0,len(child)-1)
            dna_1 = child[x]
            dna_2 = child[y]
            child[x] = dna_2
            child[y] = dna_1
            mutated_child.append(child[x])
    return mutated_child
