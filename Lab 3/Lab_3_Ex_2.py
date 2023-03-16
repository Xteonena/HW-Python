import math
import matplotlib.pyplot as plt


class circle:
    def __init__(self, center, rad):
        self.center = center
        self.radius = rad

    def area(self):
        return math.pi * self.radius ** 2

    def perimeter(self):
        return 2 * math.pi * self.radius

    def test_belongs(self, point):
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
