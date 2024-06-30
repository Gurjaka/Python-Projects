class Soda:
    def __init__(self, ingredient=None):
        if isinstance(ingredient, str):
            self.ingredient = ingredient
        else:
            self.ingredient = None
        
    def show_my_drink(self):
        if self.ingredient:
            print(f"Soda + {self.ingredient}")
        else:
            print("Ordianry soda")

# Checker
drink1 = Soda()
drink2 = Soda("კოწახური")
drink3 = Soda(5)
drink1.show_my_drink()
drink2.show_my_drink()
drink3.show_my_drink()