# Student ID: 1201200463
# Student Name: Lim Wee Zheng
import math

radius = float(input("Enter the radius : "))

volume = 4/3 * math.pi * pow(radius,3)
area = 4 * math.pi * pow(radius,2)

print("The radius of sphere: {:.2f}cm".format(radius))
print("The area of sphere: {:.2f}cm^2".format(area))
print("The volume of sphere: {:.2f}cm^3".format(volume))