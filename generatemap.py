import random

x_range = 50 #Range for x-coordinates
y_range = 50 #Range for y-coordinates
locations = 10 #Number of different locations

def generate_map(x_range, y_range, locations):
    generated_map=[]
    for x in range(locations):
        generated_map.append((random.randint(-(x_range),x_range),random.randint(-(y_range),y_range)))
    print(generated_map)
    return generated_map

generate_map(x_range,y_range,locations)




