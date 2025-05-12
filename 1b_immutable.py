# --- 2. Immutable Data ---
print("--- 2. Immutable Data ---")
# Immutability means data cannot be changed after it's created.
# Operations on immutable data create new data instances.

# Imperative: Modifying data in-place (using a list, which is mutable)
person_details_mutable = ["Alice", 30] # [name, age]

def celebrate_birthday_mutable(person):
    person[1] += 1 # Modifies the original list directly

# Functional Style: Creating new data instead of modifying the original
# (Even if using a mutable type like list, the style is to return a new one)
person_details_immutable_style_v1 = ["Bob", 25] # [name, age]

def celebrate_birthday_immutable_style(person):
    # Create a new list with the updated age
    new_name = person[0]
    new_age = person[1] + 1
    return [new_name, new_age] # Returns a new list

print("Demonstrating Immutable Data Style:")
print(f"Mutable: Initial person_details_mutable: {person_details_mutable}")
celebrate_birthday_mutable(person_details_mutable)
print(f"Mutable: After birthday: {person_details_mutable} (original list changed)")

print(f"Immutable Style: Initial person_details_immutable_style_v1: {person_details_immutable_style_v1}")
person_details_immutable_style_v2 = celebrate_birthday_immutable_style(person_details_immutable_style_v1)
print(f"Immutable Style: v1 (original): {person_details_immutable_style_v1} (unchanged)")
print(f"Immutable Style: v2 (after birthday): {person_details_immutable_style_v2} (new list created)")

# Python's tuples are truly immutable:
person_tuple_v1 = ("Charlie", 40)
# person_tuple_v1[1] = 41 # This would cause a TypeError: 'tuple' object does not support item assignment

def celebrate_birthday_tuple(person_tuple):
    return (person_tuple[0], person_tuple[1] + 1) # Creates a new tuple

person_tuple_v2 = celebrate_birthday_tuple(person_tuple_v1)
print(f"Tuple Style: v1 (original): {person_tuple_v1}")
print(f"Tuple Style: v2 (after birthday): {person_tuple_v2}")


print("-" * 20)
