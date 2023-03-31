import math
import matplotlib.pyplot as plt


class circle:
    """
    This class creates a circle object and provides methods to calculate area and perimeter, as well as
    check if a point is inside the circle.
    """

    def __init__(self, center: tuple[float, float], rad: float):
        """
        Initializes a circle object with the given center and radius.

        Args:
            center (tuple): a tuple representing the (x, y) coordinates of the center of the circle.
            radius (float): a float representing the radius of the circle.
        """
        self.center = center
        self.radius = rad

    def area(self) -> float:
        """
        Calculates the area of the circle.

        Returns:
            A float representing the area of the circle.
        """
        return math.pi * self.radius ** 2

    def perimeter(self) -> float:
        """
        Calculates the perimeter of the circle.

        Returns:
            A float representing the perimeter of the circle.
        """
        return 2 * math.pi * self.radius

    def test_belongs(self, point: tuple[float, float]) -> bool:
        """
        Checks whether a given point is inside the circle or not.

        Args:
            point (tuple): a tuple representing the (x, y) coordinates of the point to be tested.

        Returns:
            A boolean value: True if the point is inside the circle, False otherwise.
        """
        x, y = point
        a, b = self.center
        return (x - a) ** 2 + (y - b) ** 2 <= self.radius ** 2


# We request the coordinates and radius of the circle from the user
center_x = float(input("Enter the x coordinate of the center of the circle: "))
center_y = float(input("Enter the y coordinate of the center of the circle: "))
radius = float(input("Enter the radius of the circle: "))

# Create an instance of the circle class
c = circle((center_x, center_y), radius)

# We request the coordinates of a point from the user
point_x = float(input("Enter the x coordinate of the point: "))
point_y = float(input("Enter the y coordinate of the point: "))

# Call the test_belongs() method to check if the point belongs to the circle
if c.test_belongs((point_x, point_y)):
    print("The point belongs to the circle")
else:
    print("The point does not belong to the circle")

# Visualization
fig, ax = plt.subplots()
circle = plt.Circle(c.center, c.radius, fill=False)
ax.set_xlim(-10, 10)
ax.set_ylim(-10, 10)
ax.set_aspect('equal')
ax.add_artist(circle)
plt.show()
