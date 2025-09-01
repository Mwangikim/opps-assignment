# Base class
class Superhero:
    def __init__(self, name, power, city):
        self.name = name
        self.power = power
        self.city = city

    def introduce(self):
        print(f"I am {self.name} from {self.city}. My power is {self.power}!")

    def fight(self, villain):
        print(f"{self.name} fights {villain} using {self.power}!")

# Inheritance example – specialized superhero
class FlyingSuperhero(Superhero):
    def __init__(self, name, power, city, flying_speed):
        super().__init__(name, power, city)
        self.flying_speed = flying_speed  # additional attribute

    # Polymorphism: overriding fight method
    def fight(self, villain):
        print(f"{self.name} soars through the sky at {self.flying_speed} km/h and defeats {villain}!")

# Creating superhero objects
hero1 = Superhero("MightyMan", "Super Strength", "Nairobi")
hero2 = FlyingSuperhero("SkyQueen", "Wind Manipulation", "Mombasa", 200)

# Using methods
hero1.introduce()
hero1.fight("DarkLord")

hero2.introduce()
hero2.fight("ShadowBeast")
