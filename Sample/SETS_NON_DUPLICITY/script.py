x = ["apple", "orange", "banana", "pineapple"]

x_set = set(x)

x_hash_table ={
    hash("apple") : "apple",
    hash("orange") : "orange",
    hash("apple") : "apple",
    hash("banana") : "banana",
    hash("pineapple") : "pineapple",
}

if __name__ == "__main__":
    
    print(f"{x} is a list. \n")
    print(f"{x_set} is a set where no duplicate value exist. \n")
    print(f"{x_hash_table} is a dictionary behaving similarly to how sets actually works thus explaining why there are no duplicate values in set. \n")