"""
RECURSSION IS CREATION A WAY TO CREATE A METHOD WHICH PROVIDES SOLUTION BY CALLING THE METHOD 
WITHIN ITSELF TILL IT GIVES SOLUTION.
"""

def factorial(n):
    if n == 1 :
        return n
    return n * factorial(n-1)

if __name__ == "__main__":

    print(factorial(10))