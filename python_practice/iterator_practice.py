
# define a list
my_list = [4, 7, 0, 3]

# get an iterator using iter()
my_iter = iter(my_list)

# iterate through it using next()
print(next(my_iter)) # 4
print(next(my_iter)) # 7

# next(obj) is same as obj.__next__()
print(my_iter.__next__()) # 0
print(my_iter.__next__()) # 3
next(my_iter) # This will raise error, no items left
print(20 * '*')

############################################
############# Custom Iterator ##############
############################################
class PowTwo:
    """Class to implement an iterator of powers of two"""

    def __init__(self, max=0):
        self.max = max

    def __iter__(self):
        self.n = 0
        return self

    def __next__(self):
        if self.n <= self.max:
            result = 2 ** self.n
            self.n += 1
            return result
        else:
            raise StopIteration


# create an object
numbers = PowTwo(3)

# create an iterable from the object
i = iter(numbers)

# Using next to get to the next iterator elements
print(next(i)) # 1
print(next(i)) # 2 
print(next(i)) # 4
print(next(i)) # 8
print(next(i)) # StopIteration
