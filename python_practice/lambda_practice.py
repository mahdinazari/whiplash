# Simple lambda function
lambda_sqr = lambda x: x * x 
print(lambda_sqr(10))

# Lambda function has no name
print(20 * '*')
print(lambda_sqr.__name__) # <lambda> 

# lambda returns a function object
print(20 * '*')
string ='GeeksforGeeks' 
print(lambda string : string) # <function <lambda> at 0x7f65e6bbce18>

# lambda gets pass to print
print(20 * '*')
x ="GeeksforGeeks"
(lambda x : print(x))(x) # GeeksforGeeks

# Lambda Function with List Comprehension
print(20 * '*')
tables = [lambda x=x: x*10 for x in range(1, 11)]
for table in tables:
    print(table()) # 10 20 30 40 50 60 70 80 90 100

# Lambda Function with if-else
print(20 * '*')
Max = lambda a, b : a if(a > b) else b
print(Max(1, 2))
