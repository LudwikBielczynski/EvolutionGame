import random
import numpy as np

class population(object):
    def __init__(self, organisms_nr = 2, anchors_nr_limit = 2, muscles_nr_limit = 1):
        '''
        Initialize an population instance with a specific number of organisms.
        '''
        self.organisms_nr = organisms_nr
        self.anchors_nr_limit = anchors_nr_limit
        self.muscles_nr_limit = muscles_nr_limit
        self.population = []

        for organism_nr in range(1, self.organisms_nr):
            anchors_nr = random.randint(2, self.anchors_nr_limit)
            muscles_nr = random.randint(1, self.muscles_nr_limit)
            size = random.random()*20
            self.population.append(organism(anchors_nr, muscles_nr, size))

    def describePopulation(self):
        print("Population composed of %(organisms_nr)s organisms, with a limit on anchors number equal %(anchors_nr_limit)s and on muscles number %(muscles_nr_limit)s." % vars(self))
        for organism in self.population:
            organism.describe()
            organism.drawOrganism()


class organism(object):
    def __init__(self, anchors_nr, muscles_nr, size):
        '''
        Initialize an organism instance of specific size with a number of anchors and muscles connecting them.
        '''
        self.size = size

        self.anchors_nr = anchors_nr
        self.anchors = self.initializeAnchors()

        self.muscles_nr = muscles_nr
        self.muscles = self.initializeMuscles()


    def describe(self):
        print("Organism composed of %(anchors_nr)s anchors and %(muscles_nr)s muscles" % vars(self))
        return (self.anchors_nr, self.muscles_nr)

    def initializeAnchors(self):
        anchors = []
        for anchor_nr in range(1, self.anchors_nr + 1):
            anchors.append(anchor(anchor_nr, self.size))
        return anchors

    def describeAnchors(self):
        for anchor in self.anchors:
            (position, friction, weight, size) = anchor.describe(silent = True)
        return self.anchors

    def initializeMuscles(self):
        muscles = []
        for muscle_nr in range(1, self.anchors_nr):
            muscles.append(muscle(nr = muscle_nr, anchor_A = muscle_nr, anchor_B = muscle_nr + 1))
        for muscle_nr in range(self.anchors_nr, self.muscles_nr + 1):
            muscles.append(muscle(nr = muscle_nr, anchors_nr = self.anchors_nr))
        self.muscles_nr = len(muscles)
        return muscles

    def describeMuscles(self):
        for muscle in self.muscles:
            connection, contraction_time, contraction_speed, relaxation_time = muscle.describe()
        return self.muscles

    def drawOrganism(self):
        import matplotlib.pyplot as plt
        plt.figure(figsize=(5, 5))
        ax = plt.axes()        
        
        for anchor in self.anchors:
            (position, friction, weight, size) = anchor.describe(silent = True)
            circle = plt.Circle((position[0],position[1]), radius = (size/np.pi)**(1/2), alpha = .5)
            ax.add_patch(circle)

        from matplotlib.path import Path
        import matplotlib.patches as patches
        for muscle in self.muscles:
            connection, contraction_time, contraction_speed, relaxation_time = muscle.describe(silent = True)
            anchor_A = self.anchors[connection[0] - 1].position
            anchor_B = self.anchors[connection[1] - 1].position
            path = Path([anchor_A, anchor_B])
            #circle = plt.Circle((position[0],position[1]), radius = (size/np.pi)**(1/2), alpha = .5)
            ax.add_patch(patches.PathPatch(path, color = 'red', lw = 0.5))

        plt.xlim(0, self.size)
        plt.ylim(0, self.size)
        plt.show()

class anchor(object):
    def __init__(self, nr, size_organism):
        '''
        Initialize an anchor instance with random friction, weight and size positioned in an organism of predifined size.
        '''
        self.nr = nr
        x = random.random()*size_organism
        y = random.random()*size_organism
        self.position = (x, y)
        self.friction = random.random()
        self.weight = random.random()
        self.size = random.random()*size_organism

    def describe(self, silent = False):
        if silent == False:
            print("Anchor %(nr)s positioned in %(position)s, has friction: %(friction).2f, weight: %(weight).2f, size: %(size).2f" % vars(self))
        return (self.position, self.friction, self.weight, self.size)
    
    
class muscle(object):
    def __init__(self, nr, anchor_A = None, anchor_B = None, anchors_nr = 2):
        '''
        Initialize an muscle instance with random contraction time and speed.
        '''
        self.nr = nr
        
        if anchor_A == None:
            if anchor_B == None:
                anchors = list(range(1, anchors_nr + 1))
                anchor_A = random.choice(anchors)
            else:
                anchors = list(range(1, anchors_nr + 1))
                anchors.remove(anchor_B)
                anchor_A = random.choice(anchors)
        if anchor_B == None:
            anchors = list(range(1, anchors_nr + 1))
            anchors.remove(anchor_A)
            anchor_B = random.choice(anchors)

        self.connection = (anchor_A, anchor_B)
        self.contraction_time = random.random()
        self.contraction_speed = random.random()
        self.relaxation_time = random.random()

    def describe(self, silent = False):
        if silent == False:
            print("Muscle %(nr)s attached to anchors %(connection)s, has contraction time: %(contraction_time).2f, contraction speed: %(contraction_speed).2f, relaxation time: %(relaxation_time).2f" % vars(self))
        return (self.connection, self.contraction_time, self.contraction_speed, self.relaxation_time)
    

#organism = organism(anchors_nr = 4, muscles_nr = 10, size = 5)
#anchors_nr, muscles_nr = organism.describe()
#anchors = organism.describeAnchors()
#muscles = organism.describeMuscles()
#organism.drawOrganism()


