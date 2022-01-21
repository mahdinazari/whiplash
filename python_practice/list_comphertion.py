# Simple list comprehension
# new_list = [expression for member in iterable]
List = [character for character in 'Geeks 4 Geeks!']
print(List) # [‘G’, ‘e’, ‘e’, ‘k’, ‘s’, ‘ ‘, ‘4’, ‘ ‘, ‘G’, ‘e’, ‘e’, ‘k’, ‘s’, ‘!’]
print(20 * '*')

# Nested list comprehension
matrix = [[j for j in range(5)] for i in range(3)]
print(matrix) # [[0, 1, 2, 3, 4], [0, 1, 2, 3, 4], [0, 1, 2, 3, 4]]
print(20 * '*')

# List comprehension with if statement
# new_list = [expression for member in iterable (if conditional)]
squares = [n**2 for n in range(1, 11) if n%2==0]
print(squares) # [4, 16, 36, 64, 100]
print(20 * '*')

# List comprehension with if and else statement
# new_list = [expression (if conditional) for member in iterable]
original_prices = [1.25, -9.45, 10.22, 3.78, -5.92, 1.16]
prices = [i if i > 0 else 0 for i in original_prices]
print(prices) # [1.25, 0, 10.22, 3.78, 0, 1.16]
