"""
I have a list consisting integers and i need to remove zeros from list and append/shift it to end of list while 
mantaining order of rest of integers in list.
"""

def shiftZeros(item):
    
    for val in item:
        if val == 0:
            item.remove(val)
            item.append(0)
    return item

def shiftZerosOptimised(item):
    z=0
    new_list = []
    
    for val in item:
        if val != 0:
            new_list.append(val)
        else:
            z = z + 1
    new_list = new_list + ( z * [0] )
    return new_list


if __name__ == "__main__":
    
    import random,time
    n = 100000
    arr = [ random.randint(0,9) for _ in range(n) ]
    
    # approach 1
    start = time.time()
    x = shiftZeros(arr)
    end = time.time()
    print(end-start)

    # approach 2
    start = time.time()
    x = shiftZerosOptimised(arr)
    end = time.time()
    print(end-start)