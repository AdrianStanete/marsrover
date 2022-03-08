"""You are given the initial starting point (x,y) of a rover and the direction (N,S,E,W) it is facing.
"""
import pytest

from main import Rover, DirectionNotFound


def test_position_00_when_no_given_starting_position():
    rover = Rover()

    assert rover.x == 0
    assert rover.y == 0


def test_position_11_when_given_starting_position():
    rover = Rover(1, 1)

    assert rover.x == 1
    assert rover.y == 1


def test_direction_N_when_no_given_direction():
    rover = Rover()

    assert rover.direction == 'N'


def test_direction_E_when_given_direction():
    rover = Rover(direction='E')

    assert rover.direction == 'E'


def test_raises_exception_when_direction_not_valid():
    with pytest.raises(DirectionNotFound) as exception:
        Rover(direction='Q')

    assert "Invalid direction given. Only N,W,E,S valid." in str(exception.value)


def test_moves_forward_when_input_valid():
    rover = Rover()
    rover.move(['F'])

    assert rover.x == 0
    assert rover.y == 1


def test_moves_backwards_when_input_valid():
    rover = Rover()
    rover.move(['B'])

    assert rover.x == 0
    assert rover.y == 5


def test_moves_when_multiple_commands():
    rover = Rover()
    rover.move(['B', 'B', 'F', 'F', 'F'])

    assert rover.x == 0
    assert rover.y == 1


def test_rotates_right_when_input_valid():
    rover = Rover()
    rover.move(['R'])

    assert rover.direction == 'E'


def test_rotates_left_when_input_valid():
    rover = Rover()
    rover.move(['L'])

    assert rover.direction == 'W'


def test_connects_y_axis_edges():
    rover = Rover()
    rover.move(['B'])

    assert rover.x == 0
    assert rover.y == 5


def test_connects_x_axis_edges():
    rover = Rover()
    rover.move(['L', 'F'])

    assert rover.x == 5
    assert rover.y == 0
