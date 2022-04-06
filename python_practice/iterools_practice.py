import itertools

   
##########################################
########### count(start, step) ###########
##########################################
for i in itertools.count(5, 5):
    if i == 35:
        break
    else:
        print(i, end =" ") # 5 10 15 20 25 30
    
print(20 * '*')
##########################################
############# cycle(iterable) ############
##########################################
count = 0
for i in itertools.cycle('AB'):
    if count > 7:
        break
    else:
        print(i, end = " ") # A B A B A B A B 
        count += 1

print(20 * '*')
##########################################
########### repeat(val, num) ###########
##########################################
print (list(itertools.repeat(25, 4))) # [25, 25, 25, 25]

print(20 * '*')
##########################################
################ Product() ###############
##########################################
from itertools import product
   
print("The cartesian product using repeat:")
print(list(product([1, 2], repeat = 2))) # [(1, 1), (1, 2), (2, 1), (2, 2)]
print()
   
print("The cartesian product of the containers:")
print(list(product(['geeks', 'for', 'geeks'], '2'))) # [('geeks', '2'), ('for', '2'), ('geeks', '2')]
print()
   
print("The cartesian product of the containers:")
print(list(product('AB', [3, 4]))) # [('A', 3), ('A', 4), ('B', 3), ('B', 4)]

print(20 * '*')
##########################################
################ Permutations() ##########
##########################################
from itertools import permutations
   
print ("All the permutations of the given list is:") 
print (list(permutations([1, 'geeks'], 2))) # [(1, 'geeks'), ('geeks', 1)]
print()

print ("All the permutations of the given string is:") 
print (list(permutations('AB'))) # [('A', 'B'), ('B', 'A')]
print()
   
print ("All the permutations of the given container is:") 
print(list(permutations(range(3), 2))) # [(0, 1), (0, 2), (1, 0), (1, 2), (2, 0), (2, 1)]

print(20 * '*')
##########################################
################ Permutations() ##########
##########################################
from itertools import combinations
   
print ("All the combination of list in sorted order(without replacement) is:") 
print(list(combinations(['A', 2], 2))) # [('A', 2)]
print()
   
print ("All the combination of string in sorted order(without replacement) is:")
print(list(combinations('AB', 2))) # [('A', 'B')]
print()
   
print ("All the combination of list in sorted order(without replacement) is:")
print(list(combinations(range(2), 1))) # [(0, ), (1, )]

print(20 * '*')
##########################################
#### combinations_with_replacement() #####
##########################################
from itertools import combinations_with_replacement
   
print ("All the combination of string in sorted order(with replacement) is:")
print(list(combinations_with_replacement("AB", 2))) # [('A', 'A'), ('A', 'B'), ('B', 'B')]
print()
   
print ("All the combination of list in sorted order(with replacement) is:")
print(list(combinations_with_replacement([1, 2], 2))) # [(1, 1), (1, 2), (2, 2)]
print()
   
print ("All the combination of container in sorted order(with replacement) is:")
print(list(combinations_with_replacement(range(2), 1))) # [(0, ), (1, )]

print(20 * '*')
##########################################
################## accumulate() ##########
##########################################
import itertools
import operator
 
# initializing list 1
li1 = [1, 4, 5, 7]
   
# using accumulate()
# prints the successive summation of elements
print ("The sum after each iteration is : ", end ="")
print (list(itertools.accumulate(li1))) # [1, 5, 10, 17]
   
# using accumulate()
# prints the successive multiplication of elements
print ("The product after each iteration is : ", end ="")
print (list(itertools.accumulate(li1, operator.mul))) # [1, 4, 20, 140]
   
# using accumulate()
# prints the successive summation of elements
print ("The sum after each iteration is : ", end ="") # [1, 5, 10, 17]
print (list(itertools.accumulate(li1)))
   
# using accumulate()
# prints the successive multiplication of elements
print ("The product after each iteration is : ", end ="")
print (list(itertools.accumulate(li1, operator.mul))) # [1, 4, 20, 140]


print(20 * '*')
##########################################
#################### chain() #############
##########################################
import itertools
 
# initializing list 1
li1 = [1, 4, 5, 7]
   
# initializing list 2
li2 = [1, 6, 5, 9]
   
# initializing list 3
li3 = [8, 10, 5, 4]
 
# using chain() to print all elements of lists
print ("All values in mentioned chain are : ", end ="")
print (list(itertools.chain(li1, li2, li3))) # [1, 4, 5, 7, 1, 6, 5, 9, 8, 10, 5, 4]

print(20 * '*')
##########################################
########### chain.from_iterable() ########
##########################################
import itertools
 
# initializing list 1
li1 = [1, 4, 5, 7]
   
# initializing list 2
li2 = [1, 6, 5, 9]
   
# initializing list 3
li3 = [8, 10, 5, 4]
   
# initializing list of list
li4 = [li1, li2, li3]
 
# using chain.from_iterable() to print all elements of lists
print ("All values in mentioned chain are : ", end ="")
print (list(itertools.chain.from_iterable(li4))) # [1, 4, 5, 7, 1, 6, 5, 9, 8, 10, 5, 4]

print(20 * '*')
##########################################
############ itertools.compress) #########
##########################################
import itertools

# using compress() selectively print data values
print ("The compressed values in string are : ", end ="")
print (list(itertools.compress('GEEKSFORGEEKS', [1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0]))) # ['G', 'F', 'G']

print(20 * '*')
##########################################
############ dropwhile(func, seq) ########
##########################################
import itertools
 
 
# initializing list 
li = [2, 4, 5, 7, 8, 10]
   
# using dropwhile() to start displaying after condition is false
print ("The values after condition returns false : ", end ="")
print (list(itertools.dropwhile(lambda x : x % 2 == 0, li))) # [5, 7, 8, 10]

print(20 * '*')
##########################################
########## filterfalse(func, seq) ########
##########################################
import itertools
   
# initializing list 
li = [2, 4, 5, 7, 8]
 
# using filterfalse() to print false values
print ("The values that return false to function are : ", end ="")
print (list(itertools.filterfalse(lambda x : x % 2 == 0, li))) # [5, 7]

print(20 * '*')
##########################################
############ itertools.islice ############
##########################################
import itertools
   
# initializing list 
li = [2, 4, 5, 7, 8, 10, 20]
print ("The sliced list values are : ", end ="")
print (list(itertools.islice(li, 1, 6, 2))) # [4, 7, 10]

print(20 * '*')
##########################################
######## starmap(func., tuple list) ######
##########################################
import itertools
   
li = [ (1, 10, 5), (8, 4, 1), (5, 4, 9), (11, 10, 1) ]
print ("The values acc. to function are : ", end ="")
print (list(itertools.starmap(min, li))) # [1, 4, 4, 1]

print(20 * '*')
##########################################
######## takewhile(func, iterable) ######
##########################################
import itertools
   
# initializing list 
li = [2, 4, 6, 7, 8, 10, 20]
   
# using takewhile() to print values till condition is false.
print ("The list values till 1st false value are : ", end ="")
print (list(itertools.takewhile(lambda x : x % 2 == 0, li ))) # [2, 4, 6]

print(20 * '*')
##########################################
########### tree(func, iterable) #########
##########################################
import itertools
   
# initializing list 
li = [2, 4, 6, 7, 8, 10, 20]
   
# storing list in iterator
iti = iter(li) 
   
# using tee() to make a list of iterators
# makes list of 3 iterators having same values.
it = itertools.tee(iti, 3)
   
# printing the values of iterators
print ("The iterators are : ")
for i in range (0, 3):
    print (list(it[i]))
    
# [2, 4, 6, 7, 8, 10, 20]
# [2, 4, 6, 7, 8, 10, 20]
# [2, 4, 6, 7, 8, 10, 20]

print(20 * '*')
##########################################
# zip_longest( iterable1, iterable2, fillval) #
##########################################
import itertools
   
# using zip_longest() to combine two iterables.
print ("The combined values of iterables is  : ")
print (*(itertools.zip_longest('GesoGes', 'ekfrek', fillvalue ='_' ))) 
# ('G', 'e') ('e', 'k') ('s', 'f') ('o', 'r') ('G', 'e') ('e', 'k') ('s', '_')
