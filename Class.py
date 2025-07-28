from math import pi

class Circle:
    BASIC_RADIUS = 12
    def __init__(self, radius):
        self.radius = radius

    def area_calculation(self):
        return pi * (self.radius)**2 



circle = Circle(43)

print(circle)

print(f"The attribute named radius: {circle.radius}")
print(f"The method named area_calcultion: {circle.area_calculation()}")

circle.radius = 1000

print(f"The attribute named radius and radius changed to 1000: {circle.radius}")
print(f"The method named area_calcultion with radius 1000: {circle.area_calculation()}")



