from enum import Enum
from app.planet import Planet

class RoverOrientation(Enum):
    NORTH = 'N'
    SOUTH = 'S'
    EAST = 'E'
    WEST = 'W'

class Position:
  x: int
  y: int
  orientation: RoverOrientation

class Rover:
  position: Position
  planet: Planet

  def __init__(self):
    self.set_default_position()

  def land(self, planet: Planet):
    self.planet = planet

  def set_default_position(self):
    self.position = Position()
    self.position.x = 0
    self.position.y = 0
    self.position.orientation = RoverOrientation.NORTH    

  def move(self, command: str = ""):
    if command == "":
      self.set_default_position()
    elif command.lower() == 'r':
      self.position.orientation = RoverOrientation.EAST
    elif command.lower() == 'l':
      self.position.orientation = RoverOrientation.WEST

