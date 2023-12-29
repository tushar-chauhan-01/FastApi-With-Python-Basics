def makeEven(num):
    
    if num % 2 == 1 :
        return num+1
    else :
        return num
    
val = [1, 34, 543 , 54, 6543, 356, 71]

# MAP FUNCTION RETURNS AN ITERATOR THAT APPLIES FUNCTION TO EVERY ITEM OF ITERABLE
if __name__ == "__main__":
    
    even_val = list(map(makeEven, val))
    print(even_val)
