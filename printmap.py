import turtle
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

def turtle_function(selected_map):
    turtle.speed(1)
    turtle.pencolor("blue")
    turtle.pensize(2)
    sizeofmap = len(selected_map)
    i=1
    turtle.penup()
    turtle.goto(selected_map[0])
    while i+1 < sizeofmap:
        turtle.pendown()
        turtle.goto(selected_map[i])
        turtle.goto(selected_map[i+1])
        i+=1
        turtle.penup()
turtle_function(generate_map(x_range,y_range,locations))
