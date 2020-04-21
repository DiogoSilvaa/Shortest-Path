import random
import copy

x_range = 50 #Range for x-coordinates
y_range = 50 #Range for y-coordinates
locations = 10 #Number of different locations
population = 49

def generate_map(x_range, y_range, locations):
    generated_map=[]
    for x in range(locations):
        generated_map.append((random.randint(-(x_range),x_range),random.randint(-(y_range),y_range)))
    print(generated_map)
    return generated_map

def create_population(population, selected_map):
    gene_pool=[]
    for x in range(population):
        gene_pool.append(copy.deepcopy(selected_map))
        random.shuffle(gene_pool[x])
    print(gene_pool)
create_population(population, generate_map(x_range, y_range, locations))




    #gene_pool = (copy.deepcopy(selected_map))
    #random.shuffle(gene_pool)
    #print (gene_pool)
    #return gene_pool
    
