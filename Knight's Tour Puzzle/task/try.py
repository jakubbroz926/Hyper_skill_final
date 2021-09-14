possible_coordinates = ((-2, 1), (-2, -1), (-1, 2), (-1, -2), (2, 1), (2, -1), (1, 2), (1, -2))
x = 1
y = 1
coordinates = [(x+xi,y+yi) for xi,yi in possible_coordinates if (0 <= (x+xi) <= 3) and 0 <= (y+yi) <= 3 ]
print(coordinates)