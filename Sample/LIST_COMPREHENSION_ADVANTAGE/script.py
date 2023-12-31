"""
List comprehension is much more time efficient that normal traversing of iterable
"""

def forLoop(n):
    my_list = []
    for val in range(n):
        my_list.append(val)  
    return my_list

def listComp(n):
    return [ x for x in range(n) ]

def testing(number_of_time_to_test):
    forLoop_time = []
    listComp_time = []
    
    for i in range(number_of_time_to_test):
        
        import time,random
        n = random.randint(10_00_000,50_00_000)
        
        start = time.perf_counter()
        _ = forLoop(n)
        forLoop_time.append( time.perf_counter() - start )
        
        start = time.perf_counter()
        _ = listComp(n)
        listComp_time.append( time.perf_counter() - start )
        
    forLoop_avg = sum(forLoop_time)/number_of_time_to_test
    listComp_avg = sum(listComp_time)/number_of_time_to_test
    
    print( f"Average time taken by forLoop function is {forLoop_avg} and for listComp it is {listComp_avg}" )



if __name__ == "__main__":
    
    testing(250)
    
    
    