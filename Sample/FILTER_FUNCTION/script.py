"""
SIMILAR to MAP function . Filter function returns value out of iterable based on some criteria.
"""

food_item_dict ={
    "Apple" : {
        "protein" : 21,
        "fat" : 9,
        "carbs" : 13,
    },
    "Burger" : {
        "protein" : 12,
        "fat" : 350,
        "carbs" : 120,
    },
    "Pizza" : {
        "protein" : 14,
        "fat" : 456,
        "carbs" : 678,
    },
    "Salad" : {
        "protein" : 56,
        "fat" : 25,
        "carbs" : 19,
    }
}


def best_protein_diet(food_item):
    if food_item_dict[food_item]["protein"] > 15 and food_item_dict[food_item]["fat"] < 52:
        return True
    return False

vals = list(filter(best_protein_diet,food_item_dict ))

if __name__ == "__main__":
    
    print(vals) #['Apple', 'Salad']