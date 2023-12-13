class Phone:
    def __init__(self, brand, model, color):
        self.brand = brand
        self.model = model
        self.color = color

    def make_call(self, number):
        print(f"{self.brand} {self.model} is making a call to {number}")

    def receive_call(self, number):
        print(f"{self.brand} {self.model} is receiving a call from {number}")

    def send_text(self, number, message):
        print(f"{self.brand} {self.model} is sending a text to {number}: {message}")

class SmartPhone(Phone):
    def __init__(self, brand, model, color, os):
        super().__init__(brand, model, color)
        self.os = os

    def browse_internet(self):
        print(f"{self.brand} {self.model} is browsing the internet")

    def run_app(self, app_name):
        print(f"{self.brand} {self.model} is running the {app_name} app")

class BasicPhone(Phone):
    def __init__(self, brand, model, color):
        super().__init__(brand, model, color)

    def play_ringtone(self):
        print(f"{self.brand} {self.model} is playing a ringtone")


# Example usage:
smartphone = SmartPhone("Samsung", "Galaxy S21", "Black", "Android")
basicphone = BasicPhone("Nokia", "3310", "Blue")

smartphone.make_call("123-456-7890")
smartphone.run_app("Maps")
basicphone.receive_call("987-654-3210")
basicphone.play_ringtone()
