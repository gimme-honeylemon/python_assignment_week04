# import utilities.string_operations as string_operations

# major ="Robotic and AI"

# print("Original String:", major)
# print("Reversed:", string_operations.reverse_string(major))
# print("Capitalized:", string_operations.capitalize_string(major))
# print("Uppercase:", string_operations.to_uppercase(major))
# print("Lowercase:", string_operations.to_lowercase(major))
from utilities.calculator import add as add_def, subtract as subtract_def, multiply as multiply_def, divide as divide_def
from utilities.string_operations import reverse_string, capitalize_string, to_lowercase, to_uppercase
print("Using calculator.py:")
print("Addition:", add_def(10, 5))
print("Subtraction:", subtract_def(10, 5))
print("Multiplication:", multiply_def(10, 5))
print("Division:", divide_def(10, 5))

sample_string = "hello World"
print("\nUsing string_operations.py:")
print("Original:", sample_string)
print("Reversed:", reverse_string(sample_string))
print("Capitalized:", capitalize_string(sample_string))
print("Lowercase:", to_lowercase(sample_string))
print("Uppercase:", to_uppercase(sample_string))