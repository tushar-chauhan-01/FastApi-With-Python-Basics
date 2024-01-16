

def hello(name=None):
    name = name or "EXAMPLE-NAME"
    print(f"Hello {name}\n")
    
    data={
        "name":"abcd",
        "age":34
    }
    age = data["age"] or "empty age"
    names = data.get("names", "No key names in data")
    print(age,names)
if __name__ == "__main__" :
    
    hello("RAJ")
    
    print(dir(),"\n")
    # ['__annotations__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__']
    
    print(f"Script1's __name__ is equal to {__name__}\n")
    # Script1's __name__ is equal to __main__