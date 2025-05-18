# reduce() Exercise
#
# Given a list of booleans, use reduce() and a lambda to determine if
# at least one of the values in the list is True.
# Test it with all 3 lists.

flags1 = [True, False, True, True]
flags2 = [False, False]
flags3 = []

from functools import reduce


test1 = reduce(lambda x, y: x or y, flags1)
test2 = reduce(lambda x, y: x or y, flags2)
test3 = reduce(lambda x, y: x or y, flags3,False)
print(test1)  # True
print(test2)  # False
print(test3)  # False