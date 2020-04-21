import random
import copy
import math

x_range = 50 #Range for x-coordinates
y_range = 50 #Range for y-coordinates
locations = 10 #Number of different locations

def generate_map(x_range, y_range, locations):
    generated_map=[]
    for x in range(locations):
        generated_map.append((random.randint(-(x_range),x_range),random.randint(-(y_range),y_range)))
    print(generated_map)
    return generated_map

def calculate_distance(starting_x, starting_y, destination_x, destination_y):
    distance = math.hypot(destination_x - starting_x, destination_y - starting_y)  # calculates Euclidean distance (straight-line) distance between two points
    return distance

def nearestneighbour(selected_map):
    templist= copy.deepcopy(selected_map)
    optimizedlist=[]
    optimizedlist.append(templist.pop())
    for x in range(len(templist)):
        nearest_value = 10000
        nearest_index = 0
        for i in range(len(templist)):
            current_value = calculate_distance(selected_map[x][0],selected_map[x][1],selected_map[i][0],selected_map[i][1])
            if nearest_value > current_value:
                nearest_value = current_value
                nearest_index = i
        optimizedlist.append(templist[nearest_index])
        del templist[nearest_index]
    return optimizedlist
