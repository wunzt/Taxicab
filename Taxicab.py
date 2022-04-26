# Author: Thomas Wunz
# GitHub username: wunzt
# Date: 4/24/2022
# Description: Class tracks location and odometer of a Taxi in 2d space based on x and y coordinates.

class Taxicab:
    """Tracks location and odometer of a Taxi in 2d space based on x and y coordinates."""

    def __init__(self, x_coord, y_coord):
        """Creates a taxi object with an x coordinate, y coordinate, and odometer."""
        self._x_coord = x_coord
        self._y_coord = y_coord
        self._odometer = 0

    def get_x_coord(self):
        """Returns the x coordinate."""
        return self._x_coord

    def move_x(self, move_x):
        """Sets the taxi to a new x coordinate and tracks movement on odometer."""
        self._x_coord += move_x
        self._odometer += abs(move_x)

    def get_y_coord(self):
        """Returns the y coordinate."""
        return self._y_coord

    def move_y(self, move_y):
        """Sets the taxi to a new y coordinate and tracks movement on odometer."""
        self._y_coord += move_y
        self._odometer += abs(move_y)

    def get_odometer(self):
        """Returns the odometer value."""
        return self._odometer