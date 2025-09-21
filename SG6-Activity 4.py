full_name = input("Enter your full name (First, Middle, Last): ")

first, middle, last = full_name.split(", ")

first = first.capitalize()
middle_initial = middle[0].upper() + "."
last = last.title()

print("Formatted Name:", f"{last}, {first} {middle_initial}") 