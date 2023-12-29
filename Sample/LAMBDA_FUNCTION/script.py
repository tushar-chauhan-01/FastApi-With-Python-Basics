# just like list comprehension lambda can be called function comprehension
# lambda function is an alternate compact way to write an actual function

def addNum(*args):
    print(sum(args))
    
addNum1 = lambda *args: print(sum(args))

addNum2 = lambda x,y,z : print(x+y+z)

if __name__ == "__main__":
    addNum(2,3,4)
    addNum1(2,3,4)
    addNum2(2,3,4)