import enum
import random


@enum.unique
class SubstrateTypes(enum.Enum):
    grass = 0
    sand = 1
    rock = 2
    water = 3
    ice = 4
    space = 5


@enum.unique
class Features(enum.Enum):
    # TODO: Maybe separate out into individual types of features and their densities.
    empty = 0
    bush = 1
    forest = 2
    jungle = 3
    road = 4
    ruins = 5
    town = 6
    city = 7

@enum.unique
class Difficulty(enum.Enum):
    easy = 0
    difficult = 1





class Terrain(object):
    def __init__(self, substrate=SubstrateTypes.grass, features=Features.empty, elevation=0, difficulty=0):
        self.substrate = substrate
        self.elevation = elevation
        self.features = features
        self.difficulty = difficulty

    
    @staticmethod
    def choose_random_terrain():
        random_terrain_seed = random.randint(0, 100)

        # TODO: Add in ability to do weighted randomness of terrain based on map, overall terrain type.

        substrate = SubstrateTypes.grass
        if 0 < random_terrain_seed < 20:
            substrate = SubstrateTypes.space
        # elif 20 < random_terrain_seed < 25:
        #     substrate = SubstrateTypes.rock
        elif 50 < random_terrain_seed < 60:
            substrate = SubstrateTypes.water
        # elif 70 < random_terrain_seed < 90:
        #     substrate = SubstrateTypes.sand
        # elif 90 < random_terrain_seed < 100:
        #     substrate = SubstrateTypes.ice
        if 0 < random_terrain_seed < 20:
            substrate = SubstrateTypes.sand
        elif 20 < random_terrain_seed < 25:
            substrate = SubstrateTypes.rock
        elif 50 < random_terrain_seed < 60:
            substrate = SubstrateTypes.water
        elif 70 < random_terrain_seed < 90:
            substrate = SubstrateTypes.sand

        # TODO Add in features selection, add in heighted randomness
        features = Features.empty
        if 0 < random_terrain_seed < 20:
            features = Features.forest
        elif 20 < random_terrain_seed < 25:
            features = Features.bush
        elif 50 < random_terrain_seed < 60:
            features = Features.jungle
        elif 70 < random_terrain_seed < 90:
            features = Features.ruins
        elif 90 < random_terrain_seed < 100:
            features = Features.city

        elevation = random.randint(-5, 5)

        difficulty = Difficulty.easy
        if 0 < random_terrain_seed < 50:
            difficulty = Difficulty.easy
        elif 50 < random_terrain_seed < 10:
            difficulty = Difficulty.difficult
            
        return Terrain(substrate=substrate, features=features, elevation=elevation, difficulty=difficulty)

        
        

    def description(self):
        return "\n".join([self.substrate.name,self.features.name,self.difficulty.name])
    
    def full_description(self):
       return [self.substrate,self.features,format(self.elevation),format(self.difficulty)]

#"height: {}".format(self.elevation)