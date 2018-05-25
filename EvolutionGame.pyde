#TODO: Use Springs example for the muscle action.

import random
from organismEvolutionGame import Population

width = height = 600
height_horizon = 4./5
x0 = width/2
y0 = height*height_horizon

population = Population(organisms_nr = 10, 
                        anchors_nr_limit = 5, 
                        muscles_nr_limit = 15, 
                        size_limit = 500,
                        active_window=(x0, y0))
print(population.describePopulation())



def setup():
    size(width, height)
    colorMode(RGB)
    noStroke()

    fill(85, 192, 25)   
    rect(0, 0, width, height)

    fill(85, 192, 255)
    rect(0, 0, width, y0)    
    
    population.organisms[0].initialDisplay(x0, y0)
            
def draw():
    fill(85, 192, 25)   
    rect(0, 0, width, height)

    fill(85, 192, 255)
    rect(0, 0, width, y0) 

    population.organisms[0].update()
    population.organisms[0].display()
    
    fill(frameCount % 255)
    ellipse(mouseX, mouseY, 10, 10)

#    print(mouseX, mouseY)