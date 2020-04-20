import random
import turtle
import math
import copy


#Starting Data
x_range = 50 #minimum range
y_range = -50 #maximum range
locations = 10 #Number of different locations



def student_details():
    
    # add variables to store student ID and username to be returned
    student_id = 17071828
    username = dd18aaz
    return student_id, student_username

def random_gen(x_range,y_range):
    #Generate random coordinates
    randomcoordinate = (random.randint(x_range,y_range),random.randint(x_range,y_range))
    return randomcoordinate

def loop_pop(locations):
    #Creates a list and randomly populates it
     pop_list=[]
     for x in range(locations):
         pop_list.append(random_gen(y_range,x_range))
     return pop_list

def generate_map(x_range, y_range, locations):
    # add code to create a list then use a for loop to create a random population for this list
            generated_map = (loop_pop(locations))
    return generated_map

def print_map(speed, color, thickness, selected_map):
    print("printing map")

    # add code to use the turtle to draw the path between all destinations
    # the turtle should make use of the parameters provided: speed. color, etc...
    # you will need to use a loop in order to draw the path to all locations
    
def calculate_distance(starting_x, starting_y, destination_x, destination_y):
    distance = math.hypot(destination_x - starting_x, destination_y - starting_y)  # calculates Euclidean distance (straight-line) distance between two points
    return distance

def calculate_path(selected_map):

    # you will need to setup a variable to store the total path distance
    # you will need to use a loop in order to calculate the distance of the locations individually
    # it would be wise to use make use of the calculate_distance function as you can reuse this
    # remember your need to calculate the path of all locations returning to the original location

    return distance

#################################################################################################

def nearest_neighbour_algorithm(selected_map):

    temp_map = copy.deepcopy(selected_map)

    # you need to create an empty list for your optimised map 
    for x in range(len(temp_map)):

        # you need to add some variables to store establish the closest location
        
        for i in range(len(temp_map)):
            temp = i # NOTE: you can remove this line once function is implemented
            # you need to calculate the distance between the current path and the next potential location
            # it would be wise to use make use of the calculate_distance function

                # you will need to write an if statement to establish if the current distance is lower than the stored
                # best distance, and if so set the best distance to the current location

        # the final step is to add the closest location to the optermised_map and remove from the temp_map
        
    return optermised_map

#################################################################################################

def genetic_algorithm(selected_map, population, iterations, mutation_rate, elite_threshold):

    # this is the main genetic algorithm function and should make use of the inputs and call the sub functions in order to run

    # you will need to call the create_population function and store this in a list

    # you will then need to use the iterator function and store the returned solution to best_solution

    return best_solution

def create_population(population, selected_map):

    # you need to create an empty list called gene_pool for the population

    # use a for loop and the provided inputs to create the population 

    # you will also need to randomise the individuals within the population
        
    return gene_pool

def fitness_function(gene_pool, best_solution):

    # you need to find a way to rank the fitness of your population. one way you may consider doing this is with a ranked list

    # you will need to have correctly implemented the calculate_path function in order to rank the fitness of the population

    # you may consider using a loop to achieve this

    # your function must return a sorted gene pool that is sorted by fittest (shortest path to longest path

    # your function should also return the fittest individual in best_solution
    
    return sorted_gene_pool, best_solution

def iterator(gene_pool, iterations, mutation_rate, elite_threshold):

    # you need to use the provided inputs to iterate (run) the algorithm for the specified iterations

    # you will need to use a for loop in order to achieve this

    # in order for this function to work all over parts of the algorithm must be complete

    # the function must return the best individual (best_solution) in the population

    return best_solution

def mating_function(gene_pool, best_solution, mutation_rate, elite_threshold):

    # you need to create a new list called new_gene_pool to store the newly created individuals from this function

    # you will need to use a loop in order to perform the genetic crossover and mutations for each individual

    # in order for this function to work correctly you need to select the parent genes based to create the child

    # one of the top individuals based on the elite_threshold should be selected as one of the parents

    # once both parents have been chosen the breed function should be called using both of these parents
    # this means the breed function must be working and returning a child

    # once the breed function has returned a new individual this individual needs to be mutated
    # this means you need to implement the mutate function and it must return the mutated child

    # the function must return a new generation of individuals in new_gene_pool
    
    return new_gene_pool

def breed(parent_1, parent_2):

    # you need to select random points in which to cut the genes of the parents and put them into the child

    # because the individual must contain all of the locations (this is a unique issue to the TSP) the gene selection is slightly more difficult
    
    # one suggested way is to selected portions of genetic data from one parent then fill in the remainder of locations from the other parent

    # the portion of genes selected should be random and you may want to use some for loops to achieve this

    # the function must return a child of the 2 parents containing all the locations in the original map

    return child

def mutate(child, mutation_rate):

    # this function must mutate the genes of the child based on the mutation rate provided

    # to achieve this you may want to use a for loop to go through the child

    # then use a random number with an if statement according the mutation rate

    # selected genes will then need to be swapped

    # the function must return a child containing all the locations in the original map but not as it originally arrived

    return mutated_child