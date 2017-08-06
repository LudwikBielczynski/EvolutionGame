import random
import math

class population(object):
    def __init__(self, organisms_nr = 2, anchors_nr_limit = 2, muscles_nr_limit = 1, size_limit = 100):
        '''
        Initialize an population instance with a specific number of organisms.

        Attributes:
            organisms_nr - in, number of organisms in the population,
            anchors_nr_limit - int, the maximum number of anchors present in the organism,
            muscles_nr_limit - int, the maximum number of muscles present in the organism,        

        Initializes:
            organisms_nr - in, number of organisms in the population,
            anchors_nr_limit - int, the maximum number of anchors present in the organism, even if the input is different, minimal number of anchors is 2,
            muscles_nr_limit - int, the maximum number of muscles present in the organism, minimal number of muscles is (anchors_nr - 1),
            population - list of organism objects.
        '''
        self.organisms_nr = organisms_nr
        self.anchors_nr_limit = anchors_nr_limit
        self.muscles_nr_limit = muscles_nr_limit
        self.population = []

        for organism_nr in range(1, self.organisms_nr):
            anchors_nr = random.randint(2, self.anchors_nr_limit)
            muscles_nr = random.randint(1, self.muscles_nr_limit)
            size = random.random()*size_limit
            self.population.append(organism(anchors_nr, muscles_nr, size))

    def describePopulation(self):
        '''
        Prints a short description of the population.
        '''
        print("Population composed of %(organisms_nr)s organisms, with a limit on anchors number equal %(anchors_nr_limit)s and on muscles %(muscles_nr_limit)s." % vars(self))
        for organism in self.population:
            organism.describe()

class organism(object):
    def __init__(self, anchors_nr, muscles_nr, size):
        '''
        Initialize an organism instance of specific size with a number of anchors and muscles connecting them.

        Attributes:
            anchors_nr - int, number of anchors in the organism,
            muscles_nr - int, number of muscles in the organism,
            size - int, the size of the organism.

        Initializes:
            anchors_nr - int, number of anchors in the organism,
            anchors - list of objects class anchor,
            muscles_nr - int, number of muscles in the organism,
            muscles - list of objects class muscle,
            size - int, the size of the organism.

        '''
        self.size = size

        self.anchors_nr = anchors_nr
        self.anchors = self.initializeAnchors()

        self.muscles_nr = muscles_nr
        self.muscles = self.initializeMuscles()

    def describe(self):
        '''
        Short description of the organism. 

        Returns:
            (anchors_nr, muscles_nr)
        '''
        print("Organism composed of %(anchors_nr)s anchors and %(muscles_nr)s muscles" % vars(self))
        return (self.anchors_nr, self.muscles_nr)
    #--------------------------
    #Functions related with anchors
    def initializeAnchors(self):
        '''
        Creates and returns a list of objects class anchor scaled to the size of the organism.

        Returns:
            anchors - list, objects class anchor.
        '''
        anchors = []
        for anchor_nr in range(1, self.anchors_nr + 1):
            anchors.append(anchor(anchor_nr, self.size))
        return anchors

    def describeAnchors(self):
        '''
        Prints a short description of the anchors. Returns the list of anchors attached to the organism class. 

        Returns:
            anchors - list, objects class anchor attached to the organism class.
        '''
        for anchor in self.anchors:
            (position, friction, weight, size) = anchor.describe(silent = True)
        return self.anchors
    #--------------------------
    #Functions related with muscles
    def initializeMuscles(self):
        '''
        Creates and returns a list of objects class muscle. Independently of the specified muscles_nr it creates at least the links between each of the anchor assuming that the basic structure is a chain and that all the anchors need to be attached to the organism. The rest of muscles are attached randomly between two anchors.

        Returns:
            muscles - list, objects class muscle.
        '''
        muscles = []
        for muscle_nr in range(1, self.anchors_nr):
            muscles.append(muscle(nr = muscle_nr, anchor_A = muscle_nr, anchor_B = muscle_nr + 1))
        for muscle_nr in range(self.anchors_nr, self.muscles_nr + 1):
            muscles.append(muscle(nr = muscle_nr, anchors_nr = self.anchors_nr))
        self.muscles_nr = len(muscles)
        return muscles

    def describeMuscles(self):
        '''
        Prints a short description of the muscles. Returns the list of muscles attached to the organism class. 

        Returns:
            muscles - list, objects class muscle attached to the organism class.
        '''
        for muscle in self.muscles:
            connection, contraction_time, contraction_speed, relaxation_time = muscle.describe()
        return self.muscles
    #--------------------------
    #Draw in Processing
    def initialDisplay(self, x0, y0):
        '''
        Displays in processing an organism build of anchors and muscles.
        '''
        noStroke()
        x_correction = x0 - self.size/2
        y_correction = y0 - self.size
        for anchor in self.anchors:
            (position, friction, weight, size) = anchor.describe(silent = True)
            radius = math.sqrt(size/math.pi)
            fill(255, 255, 255, 200)
            ellipse(int(position[0] + x_correction), int(position[1] + y_correction), size/4, size/4)
        for muscle in self.muscles:
            connection, contraction_time, contraction_speed, relaxation_time = muscle.describe(silent = True)
            anchor_A = self.anchors[connection[0] - 1].position
            anchor_B = self.anchors[connection[1] - 1].position
            stroke(255)
            x1 = int(anchor_A[0] + x_correction)
            y1 = int(anchor_A[1] + y_correction)
            x2 = int(anchor_B[0] + x_correction)
            y2 = int(anchor_B[1] + y_correction)
            line(x1, y1, x2, y2) 

class anchor(object):
    def __init__(self, nr, size_organism):
        '''
        Initialize an anchor instance with random friction, weight and size positioned in an organism of predifined size.

        Attributes:
            nr - int, number of the anchor,
            size_organism - int, the size of the organism needed to scale the size of anchor.

        Initializing:
            nr - int, the number of the noad
            position - tuple(float, float), specifies the initial position of the anchor in the organism,
            friction - float, a value scaled 0-1 for the friction of the anchor,
            weight - float, a value scaled 0-1 for the weigth of the anchor,
            size - float, a value scaled 0-size_organism for the size of the anchor.
        '''
        self.nr = nr
        x = random.random()*size_organism
        y = random.random()*size_organism
        self.position = (x, y)
        self.friction = random.random()
        self.weight = random.random()
        self.size = random.random()*size_organism

    def describe(self, silent = False):
        '''
        Prints a short description of the anchor. Can run silently only returning values inherent to the class.

        Returns:
            position - tuple(float, float), specifies the initial position of the anchor in the organism,
            friction - float, a value scaled 0-1 for the friction of the anchor,
            weight - float, a value scaled 0-1 for the weigth of the anchor,
            size - float, a value scaled 0-size_organism for the size of the anchor.
        '''
        if silent == False:
            print("Anchor %(nr)s positioned in %(position)s, has friction: %(friction).2f, weight: %(weight).2f, size: %(size).2f" % vars(self))
        return (self.position, self.friction, self.weight, self.size)
    
    
class muscle(object):
    def __init__(self, nr, anchor_A = None, anchor_B = None, anchors_nr = 2):
        '''
        Initialize an muscle instance attached to two different anchors with random contraction time and speed, and relaxation time.

        Attributes:
            nr - int, number of the muscle,
            anchor_A - None or int, if None a random first anchor will be chosen,
            anchor_B - None or int, if None a random second anchor will be chosen from a list of anchors excluding anchor_A,
            anchors_nr - int, number of anchors in the organism,

        Initializes:
            connection - tuple(int, int), specifies connection between specified anchors,
            contraction_time - float, a value scaled 0-1 for the contraction time of the muscle,
            contraction_speed - float, a value scaled 0-1 for the contraction speed of the muscle,
            relaxation_time - float, a value scaled 0-1 for the relaxation time of the muscle.
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
        '''
        Prints a short description of the muscle. Can run silently only returning values inherent to the class.

        Returns:
            connection - tuple(int, int), specifies connection between specified anchors,
            contraction_time - float, a value scaled 0-1 for the contraction time of the muscle,
            contraction_speed - float, a value scaled 0-1 for the contraction speed of the muscle,
            relaxation_time - float, a value scaled 0-1 for the relaxation time of the muscle.
        '''
        if silent == False:
            print("Muscle %(nr)s attached to anchors %(connection)s, has contraction time: %(contraction_time).2f, contraction speed: %(contraction_speed).2f, relaxation time: %(relaxation_time).2f" % vars(self))
        return (self.connection, self.contraction_time, self.contraction_speed, self.relaxation_time)
    