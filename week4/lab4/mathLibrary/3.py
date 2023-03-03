import math

n = int(input('Number of sides: '))
l = float(input('Length of a side: '))
area = (n * l ** 2) / (4 * math.tan(math.pi / n))
print('The area of the polygon is:', area)