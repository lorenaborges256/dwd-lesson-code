# --- 3. First-Class Functions ---
print("--- 3. First-Class Functions ---")
# In Python, functions are "first-class citizens." This means they can be:
# a) Assigned to variables
# b) Passed as arguments to other functions
# c) Returned as values from other functions

def simple_greet(name):
    return f"Hello, {name}!"

def simple_farewell(name):
    return f"Goodbye, {name}!"

# a) Assigning functions to variables
print("\na) Assigning to variables:")
# Direct use (typical way)
# print(f"Direct call: {simple_greet('World')}")

# Assigning the function `simple_greet` to a variable `greeter_var`
greeter_var = simple_greet
print(f"Call via assigned variable: {greeter_var('Pythonista')}")
# `greeter_var` now behaves just like `simple_greet`

# b) Passing functions as arguments
print("\nb) Passing functions as arguments:")

# Imperative-style (hardcoded conditional logic)
def imperative_message_generator(name, message_type):
    if message_type == "greet":
        return f"Hello, {name}!"
    elif message_type == "farewell":
        return f"Goodbye, {name}!"
    return "Unknown message type"

print(f"Imperative greet: {imperative_message_generator('Alice', 'greet')}")

# Functional-style: A function that takes another function as an argument
def use_custom_message_func(name, message_function):
    # `message_function` is expected to be a function that takes one argument (name)
    return message_function(name)

# Now we can pass `simple_greet` or `simple_farewell` to `use_custom_message_func`
greeting = use_custom_message_func("Bob", simple_greet)
farewell = use_custom_message_func("Charlie", simple_farewell)
print(f"Functional (passed simple_greet): {greeting}")
print(f"Functional (passed simple_farewell): {farewell}")


# c) Returning functions from other functions
print("\nc) Returning functions from other functions:")

# Imperative-style (returning a string result based on condition)
def get_mood_string_imp(mood):
    if mood == "happy":
        return "Feeling great today!"
    elif mood == "sad":
        return "Not feeling the best."
    else:
        return "Feeling okay."

print(f"Imperative happy mood string: {get_mood_string_imp('happy')}")

# Functional-style: A function that returns *another function*
def get_mood_formatter_fp(mood):
    # Define inner functions (these will be returned)
    def happy_formatter(person_name):
        return f"Yay! {person_name} is super happy!"
    def sad_formatter(person_name):
        return f"Oh dear, {person_name} seems a bit down."
    def neutral_formatter(person_name):
        return f"{person_name} is just chilling."

    if mood == "happy":
        return happy_formatter  # Return the function itself, not its result
    elif mood == "sad":
        return sad_formatter    # Return the function itself
    else:
        return neutral_formatter # Return the function itself

# Get the appropriate formatter function
chosen_happy_formatter = get_mood_formatter_fp("happy")
chosen_sad_formatter = get_mood_formatter_fp("sad")

# Now use the returned functions
print(f"Functional (using returned happy_formatter): {chosen_happy_formatter('Dave')}")
print(f"Functional (using returned sad_formatter): {chosen_sad_formatter('Eve')}")

# You can also call it more directly (though less readable for beginners):
# print(f"Directly using returned function: {get_mood_formatter_fp('other')('Frank')}")
