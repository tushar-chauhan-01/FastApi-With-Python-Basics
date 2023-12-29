"""
Decorators in Python are a powerful and flexible way to modify or extend the behavior of functions or methods 
without changing their actual code. They allow you to "decorate" or wrap a function with additional functionality.

In the context of decorators, a wrapper is a function that "wraps around" another function. 
It serves as an intermediate layer that adds some behavior before and/or after the execution of the 
original function. The wrapper function is typically defined inside the decorator, 
and it is responsible for calling the original function and performing any additional actions.
"""
import time

def tictoc(func):
    def wrapper(*args, **kwargs):
        t1 = time.time()
        result = func(*args, **kwargs)
        t2 = time.time() - t1
        print(f"{func.__name__} took {t2} seconds to complete.")
        return result
    return wrapper

@tictoc
def hello(name):
    print(f"Hello {name or 'EXAMPLE-NAME'}")
    time.sleep(0.1)

@tictoc
def factorial_old(n):
    val = 1
    for i in range(n+1):
        if i == 0:
            continue
        val= val*i
        time.sleep(0.1)
    print(val)
    
if __name__ == "__main__":
    hello("Raj")
    factorial_old(5)
