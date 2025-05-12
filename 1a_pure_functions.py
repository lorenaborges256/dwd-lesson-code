# --- 1. Pure Functions ---
print("--- 1. Pure Functions ---")

# Imperative (Impure) Function: Modifies external state
# This function has a "side effect" because it changes 'imperative_sum'
# which is outside the function's own scope.
# If you call it multiple times with the same 'value', 'imperative_sum' will keep changing.
imperative_sum = 0
def add_to_sum_impure(value):
    global imperative_sum  # We need 'global' to modify the variable outside
    imperative_sum += value
    # print(f"Inside impure: imperative_sum is now {imperative_sum}") # A print is also a side effect

# Functional (Pure) Function:
# - Given the same inputs, it always returns the same output.
# - It does not change any state outside itself (no side effects).
def add_pure(current_sum, value):
    new_sum = current_sum + value
    return new_sum

print("Demonstrating Pure Functions:")
print(f"Initial imperative_sum: {imperative_sum}")
add_to_sum_impure(10)
print(f"After add_to_sum_impure(10): {imperative_sum}")
add_to_sum_impure(5)
print(f"After add_to_sum_impure(5): {imperative_sum}")

initial_fp_sum = 0
sum1 = add_pure(initial_fp_sum, 10)
sum2 = add_pure(sum1, 5)
print(f"Pure: initial_fp_sum = {initial_fp_sum} (unchanged)")
print(f"Pure: sum1 (add_pure(0, 10)) = {sum1}")
print(f"Pure: sum2 (add_pure(10, 5)) = {sum2}")
# Calling with same inputs yields same output:
sum_again = add_pure(initial_fp_sum, 10)
print(f"Pure: sum_again (add_pure(0, 10)) = {sum_again} (same as sum1)")

print("-" * 20)
