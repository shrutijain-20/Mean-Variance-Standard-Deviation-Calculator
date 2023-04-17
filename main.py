# This entrypoint file to be used in development. Start by reading README.md
import mean_var_std
from unittest import main

num_list = input("Enter a list of 9 numbers separated by spaces: ")

# Split the string into individual numbers
num_strings = num_list.split()

# Convert the strings to integers using map()
num_array = list(map(int, num_strings))


print(mean_var_std.calculate(num_array))

# Run unit tests automatically
main(module='test_module', exit=False)