# Simple dictionary comprehension
keys = ['a','b','c','d','e']
values = [1,2,3,4,5] 
my_dict = { k:v for (k,v) in zip(keys, values)} 
print(my_dict) # {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
print(20 * '*')

# Dictionary comprehension with if statement
quote = "life, uh, finds a way"
unique_vowels = {i for i in quote if i in 'aeiou'}
print(unique_vowels) # {'u', 'i', 'e', 'a'}

newdict = {x: x**3 for x in range(10) if x**3 % 4 == 0}
print(newdict)
print(20 * '*')

# Dictionary comprehension with if and else statements
# {(some_key if condition else default_key):(something_if_true if condition else something_if_false) for key, value in dict_.items()}
dict1 = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6}
res = {k: ('Even' if v % 2 == 0 else 'Odd') for (k, v) in dict1.items()}
print(res) # {'a': 'Odd', 'b': 'Even', 'c': 'Odd', 'd': 'Even', 'e': 'Odd', 'f': 'Even'}
