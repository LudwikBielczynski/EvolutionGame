#TODO: Use Chain example of connected chains.
#TODO: Use BouncingBall example for the gravity.
#TODO: Use Springs example for the muscle action.

import random
from organismEvolutionGame import population

population = population(organisms_nr = 10, anchors_nr_limit = 10, muscles_nr_limit = 15, size_limit = 500)
print(population.describePopulation())

width = height = 600
height_horizon = 4./5
x0 = width/2
y0 = height*height_horizon

def setup():
    size(width, height)
    colorMode(RGB)
    noStroke()
        
def draw():
    fill(85, 192, 25)
    rect(0, 0, width, height)

    fill(85, 192, 255)
    rect(0, 0, width, y0)    
    fill(frameCount % 255)
    ellipse(mouseX, mouseY, 50, 50)
    population.population[0].initialDisplay(x0, y0)