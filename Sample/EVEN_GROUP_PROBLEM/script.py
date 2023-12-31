"""
PROBLEM : Divide a number y into x parts as evenly as possible.
ANSWER : 
1. Divide y by x and get remainder and quotient
2. Minus remainder from x and fill the remaining boxes with quotient
3. fill rest of boxes with value 1+quotient
"""

def split_integer(number,parts):
    # dividing number by parts to get quotient and remainder
    quotient, remainder = divmod(number,parts)
    
    # calculating number of parts that will be filled by quotient
    base_parts_count = parts - remainder
    
    # creating array of integers where quotient will fill base_parts_count
    base_parts = base_parts_count * [quotient]
    
    # create array of integers to fill extra parts left
    # extra_parts = remainder * [quotient + 1]
    extra_parts = [ (number - sum(base_parts)) // remainder ] * remainder
    # combine 2 arrays and return
    print(f"number - {number}, parts - {parts}, quotient - {quotient}, remainder - {remainder}, base_parts_count - {base_parts_count}, base_parts - {base_parts}, extra_parts - {extra_parts}")
    return base_parts + extra_parts



if __name__ == "__main__":
    
    print(split_integer(7,3))
    print(split_integer(10,4))
    print(split_integer(3,5))
    print(split_integer(11,7))