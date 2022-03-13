class Car():
    def __init__(self, **keyword_arguments):
        self.wheels = 4
        self.doors = 4
        self.windows = 4
        self.seats = 4
        self.color = keyword_arguments.get("color", "black")
        self.price = keyword_arguments.get("price", "$20")
    
    def __str__(self):
        return f"Car with {self.wheels} wheels"


porche = Car(color="green", price="$40")
print(porche.color, porche.price)

ferrari = Car()
ferrari.color = "Yellow"

mini = Car()
mini.color = "White"

