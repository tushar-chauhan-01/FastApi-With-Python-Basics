# THIS IS EXAMPLE OF FOOD CLASS IN PYTHON WHICH CONSIST OF METHOD TO CALCULATE AND RETURN CALORIES.
# INIT METHOD IS USED OT INITILIZE VARIABLES USED ACROSS ALL CLASS
class food():
    def __init__(self):
        self.statement = "Your intake calories for this food is "
        
    def calc_calories(self, protein, carbs, fat):
        self.protein=protein
        self.carbs=carbs
        self.fat=fat
        
        calories = self.protein*4 + self.carbs*4 + self.fat*9
        return self.statement+str(calories)
    
if __name__ == "__main__":
    
    calories_dict={}

    food_instance = food()
    calories_dict["EGGS"] = food_instance.calc_calories(25,10,5)
    calories_dict["PIZZA"] = food_instance.calc_calories(protein=5, carbs=23, fat=45)
    print(calories_dict)
