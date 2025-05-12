# Lambdas Exercise
# 
# You have a list of tuples.
# Use the built-in sorted() function with a lambda as the 'key' argument
#   to sort these points on their y-coordinate (2nd element of each tuple).
# Print out the sorted points.

points = [(1, 2), (3, 1), (5, -4), (0, 0)]
# sorted_points = sorted(points)
sorted_points = sorted(points, key=lambda x: x[1])

print(sorted_points)
