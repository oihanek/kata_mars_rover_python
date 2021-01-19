from typing import List
from enum import Enum

class PlanetType(Enum):
    MERCURY = 'Mercury'
    EARTH = 'Earth'
    MARS = 'Mars'


class Planet:
    grid: List[List]    

    def __init__(self, x: int, y:int):
        self.grid = []
         
        for i in range(0, x):
            row_x = []
            for j in range(0, y):
                row_x.append(j)                
            self.grid.append(row_x)
        
    @staticmethod        
    def factory(planet_type: PlanetType):
        if planet_type == PlanetType.MERCURY:
          return Planet(20, 20)
        elif planet_type == PlanetType.EARTH:
          return Planet(40, 40)
        elif planet_type == PlanetType.MARS:
          return Planet(60, 60)
        return None

