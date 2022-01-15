# ***********************************
# *************** map ***************
# ***********************************
numbers = [1, 2, 3, 4, 5]
doubles = map(lambda x: x * 2, numbers)
print(list(doubles)) # [2, 4, 6, 8, 10]
print(list(doubles)) # []

print(20 * '*')
names = ['john', 'david', 'james']
upper_names = map(lambda x: x.upper(), names)
print(list(upper_names)) # ['JOHN', 'DAVID', 'JAMES']

# Return double of n
print(20 * '*')
def addition(n):
    return n + n
  
# We double all numbers using map()
numbers = (1, 2, 3, 4)
result = map(addition, numbers)
print(list(result))

# Add two lists using map and lambda
print(20 * '*')
numbers1 = [1, 2, 3]
numbers2 = [4, 5, 6]
result = map(lambda x, y: x + y, numbers1, numbers2)
print(list(result)) # [5, 7, 9]

# ***********************************
# ************ filter ***************
# ***********************************
print(20 * '*')
my_list = [12, 65, 54, 39, 102, 339, 221, 50, 70, ]
result = list(filter(lambda x: (x % 13 == 0), my_list)) 
print(result) # [65, 39, 221]

# find all palindromes
print(20 * '*')
my_list = ["geeks", "geeg", "keek", "practice", "aa"]
result = list(filter(lambda x: (x == "".join(reversed(x))), my_list)) 
print(result) # ['geeg', 'keek', 'aa']

# print all anagrams of str
print(20 * '*')
from collections import Counter
my_list = ["geeks", "geeg", "keegs", "practice", "aa"]
str = "eegsk"
result = list(filter(lambda x: (Counter(str) == Counter(x)), my_list)) 
print(result) # ['geeks', 'keegs']


# ***********************************
# *************** all ***************
# ***********************************
print(20 * '*')
numbers = [0, 1, 2, 3, 4, 5, 6, 7]
print(all([x % 2 == 0 for x in numbers])) # False

# ***********************************
# *************** any ***************
# ***********************************
print(20 * '*')
numbers = [0, 1, 2, 3, 4, 5, 6, 7]
print(any([x % 2 != 0 for x in numbers])) # True

# ***********************************
# *************** zip ***************
# ***********************************