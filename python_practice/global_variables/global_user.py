import global_variable


# import global variable from external file
print (global_variable.xyz)

# import global variable from function in external file
global_variable.init()
global_variable.myList.append('hey')
print(global_variable.myList[0])
