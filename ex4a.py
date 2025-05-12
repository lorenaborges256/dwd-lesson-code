# map() Exercises
#
# Exercise 1
# ----------
# You have a list of product prices.
# Use `map` and a lambda to create a new list where each price
# has a 20% tax added to it (price * 1.20).
# Remember to format the output nicely if you can
# (e.g., to two decimal places, but the core is the map).

prices = [10.99, 5.49, 20.00]

tax_price = list(map(lambda p: p * 1.20 , prices))
print(tax_price)

# Exercise 2
# ----------
# Given a list of scores, use map() to get a list of the grade level for each score.
#
# HD if >=90
# D if >=80
# C if >=70
# P if >=50
# F if <50

scores = [85, 92, 78, 60, 42, 95, 70, 53]
grades = list(map(lambda score: 'HD' if score >= 90 else
                   'D' if score >= 80 else
                   'C' if score >= 70 else
                   'P' if score >= 50 else
                   'F', scores))
print(grades)


