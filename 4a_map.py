# Higher-order Functions: map
# ---------------------------
# map() transforms a iterable into a new iterable by applying a function to each element.
# Syntax: map(function, iterable) -> iterable (map object)
# An iterable is any object capable of being iterated over (eg. list)

numbers = [1, 2, 3, 4]

def double(n):
    return n * 2

doubled_numbers = map(double, numbers)
print(f"Doubled (def): {list(doubled_numbers)}")

tripled_numbers = map(lambda x: x * 3, numbers)
print(f"Tripled (lambda): {list(tripled_numbers)}")

# Note that map() is a pure function, so the original list is unmodified.
print(numbers)

# MODIFY
# Given a list of names get a list of greetings eg. ['Hello Alice', 'Hello Bob', ...]
names = ['alice', 'bob', 'charlie']
greetings = list(map(lambda name: f"Hello {name.capitalize()}", names))
print(greetings)
