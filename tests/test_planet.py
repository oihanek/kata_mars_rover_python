from app.planet import Planet

def test_planet_is_of_expected_size_when_regular():
    x = 10
    y = 10

    planet = Planet(x, y)
    assert len(planet.grid) == x
    assert len(planet.grid[0]) == y


def test_planet_is_of_expected_size_when_irregular():
    x = 11
    y = 10

    planet = Planet(x, y)
    assert len(planet.grid) == x
    assert len(planet.grid[0]) == y    