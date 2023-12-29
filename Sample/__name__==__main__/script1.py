

def hello(name=None):
    name = name or "EXAMPLE-NAME"
    print(f"Hello {name}\n")
    
if __name__ == "__main__" :
    
    hello("Raj 1")
    
    print(dir(),"\n")
    # ['__annotations__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__']
    
    print(f"Script1's __name__ is equal to {__name__}\n")
    # Script1's __name__ is equal to __main__