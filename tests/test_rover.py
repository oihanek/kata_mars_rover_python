from app.rover import Rover, RoverOrientation
from app.planet import PlanetType, Planet

def test_rover_initialization():
    rover = Rover()
    assert(rover.position.x == 0)
    assert(rover.position.y == 0)
    assert(rover.position.orientation == RoverOrientation.NORTH)

def test_rover_position_empty():
    rover = Rover()
    rover.position.x = 10
    rover.move()
    assert(rover.position.x == 0)
    assert(rover.position.y == 0)
    assert(rover.position.orientation == RoverOrientation.NORTH)

def test_rover_turns_right():
    rover = Rover()    
    rover.move('r')
    assert(rover.position.x == 0)
    assert(rover.position.y == 0)
    assert(rover.position.orientation == RoverOrientation.EAST)

def test_rover_lands_on_planet():
    planet = Planet.factory(PlanetType.MARS)
    rover = Rover()  
    rover.land(planet)
    assert rover.planet == planet
