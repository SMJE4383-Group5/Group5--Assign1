class HotDrink:
    def __init__(self, name, temperature):
        self.name = name
        self.temperature = temperature

class Coffee(HotDrink):
    def __init__(self, name, temperature, roast_level):
        super().__init__(name, temperature)
        self.roast_level = roast_level

    def info(self):
        return f"{self.name} - Roast Level: {self.roast_level}, Temperature: {self.temperature}C"

class Tea(HotDrink):
    def __init__(self, name, temperature, type_of_tea):
        super().__init__(name, temperature)
        self.type_of_tea = type_of_tea

    def info(self):
        return f"{self.name} - Tea Type: {self.type_of_tea}, Temperature: {self.temperature}C"

class HotChocolate(HotDrink):
    def __init__(self, name, temperature, chocolate_intensity):
        super().__init__(name, temperature)
        self.chocolate_intensity = chocolate_intensity

    def info(self):
        return f"{self.name} - Chocolate Intensity: {self.chocolate_intensity}, Temperature: {self.temperature}C"


my_coffee = Coffee("Espresso", 80, "Dark")
my_tea = Tea("Green Tea", 70, "Green")
my_hot_chocolate = HotChocolate("Classic Hot Chocolate", 65, "Medium")


print(my_coffee.info())            
print(my_tea.info())              
print(my_hot_chocolate.info())     
