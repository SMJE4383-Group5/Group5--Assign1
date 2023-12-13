class HotDrink:
    def __init__(self, name, temperature):
        self.name = name
        self.temperature = temperature

    def describe(self):
        print(f"{self.name}- Temperature: {self.temperature} degrees Celsius.")

class Coffee(HotDrink):
    def __init__(self, coffee_type, temperature):
        super().__init__('Coffee', temperature)
        self.coffee_type = coffee_type

    def describe(self):
        super().describe()
        print(f"Type: {self.coffee_type}.")

class Tea(HotDrink):
    def __init__(self, tea_type, temperature):
        super().__init__('Tea', temperature)
        self.tea_type = tea_type

    def describe(self):
        super().describe()
        print(f"Type: {self.tea_type}.")

class HotChocolate(HotDrink):
    def __init__(self, chocolate_type, temperature):
        super().__init__('Hot Chocolate', temperature)
        self.chocolate_type = chocolate_type

    def describe(self):
        super().describe()
        print(f"Type: {self.chocolate_type}.")

# Demonstrate polymorphic behavior
coffee = Coffee('Espresso', 75)
tea = Tea('Green Tea', 80)
hot_chocolate = HotChocolate('Dark Chocolate', 65)

drinks = [coffee, tea, hot_chocolate]

for drink in drinks:
    drink.describe()
    print("\n")
