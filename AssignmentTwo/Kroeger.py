'''
CSC240- ASSIGNMENT 2- Drew Kroeger, 
This script takes length, spacing, depth of flowebeds, and depth of filled areas,
It then outputs the plants for each type of flowerbed, total number of plants for the garden
yards of soil for each type of flowebed, and total cubic yards to material for the garden
'''

import math

#these are all the input values
garden_length = float(input("Enter length of garden,in feet:"))
plant_spacing = float(input("Enter spacing between plants,in feet:"))
garden_depth = float(input("Enter the depth of the garden soil, in feet:"))
fill_depth = float(input("Enter the depth of the filled areas, in feet:"))


#based on the picture(if it is to reference), then 2 circles is the same length of the square, or 4 circle radii
circle_diameter = garden_length/2
circle_radius = garden_length/4


pi = math.pi                                                                                    #this did not want to work in the equation so i put it here
flowerbed_circle_area = (circle_radius  ** 2) * (pi)                                            #simple circle area equation
flowerbed_semicircle_area = flowerbed_circle_area/2                                             #simple semicircle area equation

area_per_plant = (plant_spacing ** 2)                                                           #this is basically a square around the plant,its personal space, but in 2D

flowerbed_circle_plants = flowerbed_circle_area/area_per_plant                                  #amount of plants that fit in a circle
flowerbed_circle_plants_truncated = math.trunc(flowerbed_circle_plants)                         #amount of plants that fit in a circle, truncated

flowerbed_semicircle_plants = flowerbed_semicircle_area/area_per_plant                          #amount of plants that fit in a semicircle
flowerbed_semicircle_plants_truncated = math.trunc(flowerbed_semicircle_plants)                 # amount of plants that fit in a semicircle,truncated

total_plants = flowerbed_circle_plants_truncated + (flowerbed_semicircle_plants_truncated*4)    #the plants that would fit in the circles and semicircles all rounded up

total_garden_area = garden_length ** 2                                                          #this is the total square area
total_filled_area = total_garden_area - (flowerbed_circle_area * 3)                             #this is the concrete area,there are full 3 circles in the area,whence the three came from
total_flowerbed_area = flowerbed_circle_area * 3                                                #three circles in the square,so total flowerbed area is three circles 

semicircle_garden_volume_in_cubic_yards = (flowerbed_semicircle_area * garden_depth) / 27       #this is the volume,not area, of the single semicircle, volume(where the plants are going), the /27 is converting from cubic feet to cubic yards
circle_garden_volume_in_cubic_yards = (flowerbed_circle_area * garden_depth) / 27               #this is volume of the big circle, where we take area and multiply bt the depth, /27 comes from converting cubic feet to cubic yards

total_filled_area_volume = (total_filled_area * fill_depth)/27                                  #this is the total fill for the garden /27 is cubic feet to cubic yards
total_garden_volume = (total_flowerbed_area * garden_depth)/27                                  #this is the total soil for the garden /27 is cubic feet to yards
print(" ")
print("GARDEN REQUIREMENTS")
print("-----------------------------")
print("Plants for each semicircle garden:", flowerbed_semicircle_plants_truncated)
print("Plants for circle garden:", flowerbed_circle_plants_truncated)
print("Total plants for garden:" , total_plants)
print("Soil for each semicircle garden:" , round(semicircle_garden_volume_in_cubic_yards,1), "cubic yards")
print("Soil for the circle garden" , round(circle_garden_volume_in_cubic_yards,1), "cubic yards")
print("Total soil for the garden:", round(total_garden_volume,1), "cubic yards")
print("Total fill for the garden:", round(total_filled_area_volume,1), "cubic yards")

#end