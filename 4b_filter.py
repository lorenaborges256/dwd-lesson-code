# Higher-order Functions: filter
# ------------------------------
# filter() creates a new list from an existing list. Elements are included in 
#   the new list if a function called on the element returns True.
# Syntax: filter(function, iterable) -> iterable (filter object)
# An iterable is any object capable of being iterated over (eg. list)

numbers = [1, 2, 3, 4, 5, 6]

def is_even(n):
    return n % 2 == 0

even_numbers = filter(is_even, numbers)
print(f"Evens (def): {list(even_numbers)}")

odd_numbers = filter(lambda x: x % 2 != 0, numbers)
print(f"Odds (lambda): {list(odd_numbers)}")

# Note that filter() is a pure function, so the original list is unmodified.
print(numbers)

# MODIFY
# Given a list of words, get a list of words with at least 5 letters.
words = ['apple', 'banana', 'kiwi', 'orange', 'fig']
long_words = list(filter(lambda word: '''your code here'''))
print(long_words)
