import random
import math

#Starting Data
x_range = 50 #minimum range
y_range = 50 #maximum range
locations = 3 #Number of different locations


def generate_map(x_range, y_range, locations):
    generated_map=[]
    for x in range(locations):
        generated_map.append((random.randint(-(x_range),x_range),random.randint(-(y_range),y_range)))
    print(generated_map)
    return generated_map

def calculate_distance(starting_x, starting_y, destination_x, destination_y):
    distance = math.hypot(destination_x - starting_x, destination_y - starting_y)  # calculates Euclidean distance (straight-line) distance between two points
    return distance

def calculate_path(selected_map):
    distance = 0
    sizeofmap = len(selected_map)
    i = 0
    while i+1 < sizeofmap:
        distance = distance + calculate_distance(selected_map[i][0],selected_map[i][1],selected_map[i+1][0],selected_map[i+1][1])
        i=i+1
    distance = distance + calculate_distance(selected_map[i][0],selected_map[i][1],selected_map[0][0],selected_map[0][1])
    print (distance)
    return distance
calculate_path(generate_map(x_range,y_range, locations))
