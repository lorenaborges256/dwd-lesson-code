# Callbacks Exercise
#
# 1. Write a function: perform_operation(a, b, math_callback).
# 2. This function should take two numbers and a callback.
# 3. The callback function itself should accept two numbers and return their result
#       (e.g., sum, product).
# 4. perform_operation() should then print this result.
# 5. Create two simple callbacks (e.g., add_them, multiply_them) and
#       test perform_operation with both.

def add_them(a, b):
    return a + b

def multiply_them(a, b):
    return a * b

def perform_operation(a, b, math_callback):
    result = math_callback(a, b)
    print(result)

perform_operation(3, 4, add_them)  # Should print 7
perform_operation(3, 4, multiply_them)  # Should print 12