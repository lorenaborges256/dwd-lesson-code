# Callback Functions

def greet(name): return f"Hello, {name}!"
def farewell(name): return f"Goodbye, {name}!"

def process_interaction(name, callback_func): # callback_func is the callback
    message = callback_func(name)
    print(message)

process_interaction("Alice", greet) #greet isn't called here, only referenced
process_interaction("Bob", farewell)

# MODIFY
# We want a new interaction: shouting a question.
# Define a *new* callback function `shout_question` and pass it to
# `process_interaction` so it prints something like 'HEY, ALICE, HOW ARE YOU?!'?"
def shout_question(name): return f"HEY, {name.upper()}, HOW ARE YOU?!"
process_interaction("Matt", shout_question)