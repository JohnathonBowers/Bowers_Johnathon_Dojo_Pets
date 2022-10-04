class Ninja:
    def __init__ (self, first_name, last_name, treats, pet_food, pet):
        self.first_name = first_name
        self.last_name = last_name
        self.treats = treats
        self.pet_food = pet_food
        self.pet = pet

    def walk(self):
        print(f"Walking {self.pet.name}!")
        self.pet.play()
        print(f"{self.pet.name}'s energy is now {self.pet.energy}")
        return self
    
    def feed(self):
        print(f"Feeding {self.pet.name} {self.pet_food}!")
        self.pet.eat()
        print (f"{self.pet.name}'s energy is now {self.pet.energy}.")
        return self

    def bathe(self):
        print(f"Giving {self.pet.name} a bath.")
        self.pet.noise()