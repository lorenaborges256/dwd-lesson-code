# Lambda Functions

# A lambda is a function that has the following properties:
# - Anonymous - Lambdas do not have a name, and don't need one.
# - Inline - No need for a 'def' because they are declared inline when needed.
# - Single expression - Cannot have multiple statements or expressions. When the
#       lambda is called, the expression is evaluated and the result
#       automatically returned (hence no need of a return statement)
#
# In all other respects they behave just like a regular function.
#
# Syntax: lambda arguments: expression

# Example 1: lambda function to calculate exponents
# Note the absence of a name, and since it's a function, we can store it in a var.
power = lambda base, exp: base ** exp
# def power(base, exp):
#     return base ** exp
# Double-asterisk (**) means 'raise to' or 'to the power of'
# power lambda could be declared like this def function^^^

# Call the lambda just like any other function
print(power(2, 3)) # 8 # power has all lambda function

# Example 2: Pass a lambda as a callback
# This is the exact same process_interaction function we used earlier
def process_interaction(name, callback_func): # callback_func is the callback
    message = callback_func(name)
    print(message)
# Call it with a lambda rather than having to def the function in advance
process_interaction("Charlie", lambda person_name: f"What's up, {person_name}?")

# MODIFY
# 1. Convert the following function into a lambda
# 2. Call process_interaction and pass the lambda to it
# def capitalize_string(s):
#     return s.capitalize()
capitalize_string = lambda s: s.capitalize()
process_interaction("anna", capitalize_string)
process_interaction("lorena", capitalize_string)