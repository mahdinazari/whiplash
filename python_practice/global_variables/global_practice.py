def func_1():
    global my_list
    my_list = [1, 2, 3]
    print(my_list)
    

def func_2():
    my_list.append(4)
    my_list.append(5)
    my_list.append(6)
    print(my_list)
    
    
func_1() # [1, 2, 3]
func_2() # [1, 2, 3, 4, 5]
