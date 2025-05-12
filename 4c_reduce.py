# Higher-order Functions: reduce
# ------------------------------
# reduce() aggregates a list to a single value by calling a function for each
#   element and accumulating the results.
# Syntax: reduce(function, iterable[, initializer]) -> iterable (reduce object)
# An iterable is any object capable of being iterated over (eg. list)

# Need to import reduce() from the stdlib (standard library)
from functools import reduce

numbers = [1, 2, 3, 4, 5]
# Note that the lambda accepts the accumulator value and the current element,
# then returns a new accumulator value.
sum_total = reduce(lambda acc, current: acc + current, numbers)
print(f"Sum: {sum_total}")

# With initializer
# Start with 1 for product
product_total = reduce(lambda acc, current: acc * current, numbers, 1)
print(f"Product: {product_total}")

# Note that filter() is a pure function, so the original list is unmodified.
print(numbers)

# MODIFY

# 1. Modify the 'sum' example above so that it starts from a base value of 10.
sum_total = reduce(lambda acc, current: acc + current, numbers)
print(f"Sum: {sum_total}")

# 2. Using the original 'sum' example, modify ONLY the lambda so that it
# concatenates a list of strings instead of summing a list of numbers.
numbers = ['hello', ' ', 'there', '!']
